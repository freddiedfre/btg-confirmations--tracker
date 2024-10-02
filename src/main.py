# src/main.py
import argparse

from src.apps import cli, web


def main():
    parser = argparse.ArgumentParser(
        description="Track BTG Transaction Confirmation Progress."
    )
    parser.add_argument("--txid", type=str, help="Transaction ID for CLI tracking")
    parser.add_argument("--web", action="store_true", help="Run the web interface")

    args = parser.parse_args()

    if args.web:
        web.run_web()
    elif args.txid:
        cli.cli_progress(args.txid)
    else:
        print(
            "Please provide a --txid for CLI tracking or use --web to run the web interface."
        )


if __name__ == "__main__":
    main()
