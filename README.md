# PR

A single server rainbow roles Discord bot (WARNING: THIS IS AGAINST THE DISCORD API'S TOS. ACTION CAN BE TAKEN ON THE BOT, BOT'S OWNER OR THE SERVER)

## version

0.1.1

## requirements

- Python interpreter 3.10

## setup

step 1: clone the repository

step 2: cd into the repository's directory

step 3: create the `conf.toml` file.

step 3.a: put your guild's (discord server) id into `conf.toml` (same directory)

```toml
guild_id = YOUR_GUILD_ID_GOES_HERE
```

step 3.b: put the role ids into `conf.toml`

```toml
role_ids = [ROLE_1_ID_GOES_HERE, ROLE_2_ID_GOES_HERE, ...]
```

step 3.c: put your bot's token into `conf.toml`

```toml
token = "YOUR_TOKEN_GOES_BETWEEN_QUOTES"
```

step 4: run the bot (bot should be invited into the guild before running or it will throw an error. the role should be present too)

```sh
python -m src.bot
```

That's it

## Memory Usage

< 30 megabytes
