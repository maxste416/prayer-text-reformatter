# prayer-text-reformatter

A small utility for converting prayer request snippets into the bullet-point format shown in the example below. It ships with a simple command-line interface and can be bundled into an offline executable with tools such as [PyInstaller](https://pyinstaller.org/).

## Example

**Input**

```
Nov 16, 2024: Nepal – Caste Discrimination and the Church

In Nepal, the caste system has long created division, excluding many from opportunities and causing discrimination and injustice. As the church grows, it has the opportunity to be a powerful witness of unity, breaking down caste barriers and showing that in Christ, all are equally valued and loved. Still some who are in Christ have not accepted this revelation of oneness.

Pray for the church in Nepal to be a place where caste barriers are broken, demonstrating the equal value of all people in Christ.

Ask for believers to lead by example, promoting love and inclusion in their communities.

Pray for those who have suffered under caste discrimination to find acceptance, healing, and hope within the body of Christ.
```

**Output**

```
*Nov 16, 2024 | Nepal – Caste Discrimination and the Church*

In Nepal, the caste system has long created division, excluding many from opportunities and causing discrimination and injustice. As the church grows, it has the opportunity to be a powerful witness of unity, breaking down caste barriers and showing that in Christ, all are equally valued and loved. Still some who are in Christ have not accepted this revelation of oneness.

- Pray for the church in Nepal to be a place where caste barriers are broken, demonstrating the equal value of all people in Christ.

- Ask for believers to lead by example, promoting love and inclusion in their communities.

- Pray for those who have suffered under caste discrimination to find acceptance, healing, and hope within the body of Christ.
```

## Installation

```bash
python -m pip install .
```

This command installs the `prayer-text-reformatter` package and exposes the `prayer-text-reformatter` CLI.

## Usage

```bash
prayer-text-reformatter input.txt output.txt
```

If the output file is omitted the reformatted text is written to standard output.

## Creating an offline executable

You can use PyInstaller to create a single-file executable (on Windows, macOS, or Linux) that runs without Python being installed.

```bash
python -m pip install pyinstaller
pyinstaller -F -n prayer-text-reformatter src/prayer_text_reformatter/cli.py
```

The resulting executable will be available in the `dist/` directory.

## Development

Install the project in editable mode and run the tests:

```bash
python -m pip install -e .
pytest
```
