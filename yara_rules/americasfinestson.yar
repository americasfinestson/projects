/*
    This Yara rule simply searches for any file matching the first line of the github.com/americasfinestson/projects/README.md

    Tested:
    >>> import yara
    >>> from pprint import pprint
    >>> rules = yara.compile('/path/to/americasfinestson.yar')
    >>> pprint(rules.match('/path/to/README.md'))
    {'main': [{'matches': True,
               'meta': {'author': 'Josh Whipkey',
                        'date': '2022-02-17',
                        'description': 'Test Yara rule - no actual malware '
                                       'signatures'},
               'rule': 'americasfinestson',
               'strings': [{'data': 'Often times, I try to create the same '
                                    'automation in bash, Python, and YAML '
                                    '(Ansible).',
                            'flags': 19,
                            'identifier': '$readme2',
                            'offset': 111},
                           {'data': 'Hello, and welcome to my Github',
                            'flags': 19,
                            'identifier': '$readme1',
                            'offset': 11}],
               'tags': []}]}
*/

rule americasfinestson
{
  meta:
    description = "Test Yara rule - no actual malware signatures"
    author = "Josh Whipkey"
    date = "2022-02-17"

  strings:
    $readme1 = "Hello, and welcome to my Github"
    $readme2 = "Often times, I try to create the same automation in bash, Python, and YAML (Ansible)."

  condition:
    $readme1 or $readme2
}

