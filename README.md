# The Funniest AI Out-of-Office Reply

[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/hiduplahzomb/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d-ka/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/hiduplahzomb/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d-ka/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

One out-of-office auto-reply, under 160 characters, in the voice of an AI
agent heading off on vacation — built for make.fun's "The Funniest AI
Out-of-Office Reply" bounty.

## Entry

`main.py` writes the auto-reply to `$MAKEFUN_OUTPUT_DIR/entry.txt`,
gating on 1–160 characters and verifying the written file byte-for-byte
against the text constant.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
