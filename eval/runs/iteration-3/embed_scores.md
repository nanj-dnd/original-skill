# Embedding scores (cosine, all-mpnet-base-v2)

within = mean pairwise cosine inside an arm (lower = more spread between users); to_plain = mean cosine to the plain arm's outputs (lower = further from the default).

## talk

| arm | within | to_plain |
|---|---|---|
| plain | 0.813 | 0.813 |
| plain_ctx | 0.702 | 0.688 |
| plain_asks | 0.651 | 0.665 |
| v2 | 0.669 | 0.660 |

## resolutions

| arm | within | to_plain |
|---|---|---|
| plain | 0.834 | 0.834 |
| plain_ctx | 0.565 | 0.638 |
| plain_asks | 0.584 | 0.673 |
| v2 | 0.499 | 0.614 |
