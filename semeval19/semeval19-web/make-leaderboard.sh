cat $1 \
  | awk 'BEGIN {
      users["semeval-pan-2019-baseline"] = 1
    }{
      if (!($1 in users)) {
        position += 1
        printf "<tr><td>%d</td><td>%s</td><td></td><td>%.3f</td><td>%.3f</td><td>%.3f</td><td>%.3f</td><td></td></tr>\n", position, $1, $5, $6, $7, $8
        users[$1] = 1
      }
    }'
