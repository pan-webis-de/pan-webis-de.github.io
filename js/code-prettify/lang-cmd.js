PR['registerLangHandler'](
    PR['createSimpleLexer'](
        [
            [PR['PR_PUNCTUATION'], /^[|<>!\\]/, null, '|<>!\\'],
            [PR['PR_COMMENT'], /^#[^\r\n]*/, null, '#'],
            ['lang-cmd', /^\$\(([^)])\)/, null, '$'],
            [PR['PR_TAG'], /^\$(?:[\w_]+\b|{[^}]+})/, null, '$'],
        ],
        [
            [PR['PR_KEYWORD'], /^(?:\/|\.\/)[^\s]+\.(?:sh|bin)\b/],
            [PR['PR_KEYWORD'], /^(?:\/usr)?\/s?bin\/\w+\b/],
            [PR['PR_KEYWORD'], /^\b(?:mySoftware|echo|cat|grep|awk|cut|tr|printf?|tail|head|break|continue|do|else|for|if|return|while|case|done|elif|esac|eval|fi|function|in|local|set|then)\b/],
            [PR['PR_ATTRIB_NAME'], /^\s--?[\w_-]+\b/],
            [PR['PR_LITERAL'], /^\s\d+\b/]
        ]),
    ['cmd']);
