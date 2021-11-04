#!/usr/bin/env bash

FAILURES=""

function print_help {
   cat <<EOF
   Use: pre-push.sh [--debug --help]
   Options:
   --check-only    Only run validations; don't change anything
   -h, --help      Show this message and exit
   -g, --debug     Show commands as they are executing
EOF
}

while (( $# ))
do
  case $1 in
    --check-only)
      CHECK_ONLY=1
      ;;
    --help|-h)
      print_help
      exit 0
      ;;
    --debug|-g)
      set -x
      ;;
    *)
      echo "Invalid Option: $1"
      print_help
      exit 1
      ;;
  esac
  shift
done

function echo_error {
  local message="$1"
  if [[ -n "${GITHUB_REF}" ]]
  then
    echo "::error::$message"
  else
    echo -e "\033[0;31m$message\033[0m"
  fi
}

function set_error {
  local message="$1"
  echo_error "$message"
  failure=$(test -z "$FAILURES" || echo ", ")
  failure="${failure}${message}"
  FAILURES="${FAILURES}${failure}"
}

tag=uw-saml-python:build

function run_black {
  docker run -v $(pwd):/data ${tag} black /data/uw_saml2 /data/tests $@
}

function blacken {
  local commit_in_progress=
  if ! run_black --check
  then
    if [[ -n "${CHECK_ONLY}" ]]
    then
      set_error "Code is not blackened"
    elif [[ -n "$(git diff)" ]]
    then
      echo "Blackening code for in-progress commit"
      run_black
    else
      echo "No commit in progress. Would you like to:"
      echo "  [a]mend the previous commit with linted code, or"
      echo "  [c]reate a new commit with linted code?"
      echo " > "
      COMMIT_ACTION=create
      while ! [[ "$REPLY" =~ ^a|c$ ]]
      do
        echo "invalid input. [a]mend the last commit or [c]reate a new one?"
        read -n1
      done
      run_black
      case "$REPLY" in
        a)
          git commit --amend --no-edit
          ;;
        c)
          git commit -m "[auto-commit] blacken python code"
          ;;
        *)
          echo "Invalid choice: $REPLY; not creating or amending a commit"
          ;;
      esac
    fi
  fi
}

docker build -t ${tag} .
blacken
docker run ${tag} pytest || set_error "Pytest failed!"
if [[ -n "${FAILURES}" ]]
then
  echo_error "Validation failed for the following reason(s): $FAILURES"
  exit 1
fi
