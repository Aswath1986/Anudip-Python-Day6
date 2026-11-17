# Facilitator

`PRACTICE_ANSWER_KEY.md.enc` is the answer key for the files in
[`Day6_Practice`](../Day6_Practice). It is encrypted (AES-256) so that students
cannot read it. The passphrase is held by the facilitator and is not in this
repository.

## Reading the key

`openssl` is already present on macOS and Linux. On Windows, use **Git Bash**,
which includes it.

```bash
cd Facilitator
openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -a \
    -in PRACTICE_ANSWER_KEY.md.enc -out PRACTICE_ANSWER_KEY.md
```

Type the passphrase when asked. The command writes `PRACTICE_ANSWER_KEY.md`,
which opens in any editor. That file is listed in `.gitignore`, so it cannot be
committed by accident.
