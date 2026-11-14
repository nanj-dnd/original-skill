# Embedding scores (cosine, all-mpnet-base-v2)

within = mean pairwise cosine inside an arm (lower = more spread between users); to_plain = mean cosine to the plain arm's outputs (lower = further from the default).

## talk

| arm | within | to_plain |
|---|---|---|
| plain | 0.813 | 0.813 |
| plain_ctx | 0.702 | 0.688 |
| quick | 0.793 | 0.722 |
| full | 0.564 | 0.595 |

## resolutions

| arm | within | to_plain |
|---|---|---|
| plain | 0.834 | 0.834 |
| plain_ctx | 0.565 | 0.638 |
| quick | 0.682 | 0.718 |
| full | 0.506 | 0.628 |
