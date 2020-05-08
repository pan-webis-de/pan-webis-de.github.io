cat $1 \
  | awk 'BEGIN {
      users["semeval-pan-2019-baseline"] = 1
    } FILENAME == "leaderboard.html" {
      if ($0 ~ /^<tr/) {
        split($0, cells, "</td><td>")
        codename = cells[2]
        if (!(codename in names)) {
          names[codename] = cells[3]
          links[codename] = cells[8]
        }
      }
    } FILENAME == "/dev/stdin" {
      if (!($1 in users)) {
        position += 1
        printf "<tr><td>%d</td><td>%s</td><td>%s</td><td>%.3f</td><td>%.3f</td><td>%.3f</td><td>%.3f</td><td>%s\n", position, $1, names[$1], $5, $6, $7, $8, links[$1]
        users[$1] = 1
      }
    }' leaderboard.html /dev/stdin
