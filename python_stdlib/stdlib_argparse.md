# argparse - Parser for command-line options

[](inv:py3#library/argparse)

## Basic

{meth}`add_argument() <argparse.ArgumentParser.add_argument>`  
{meth}`parse_args() <argparse.ArgumentParser.parse_args>`

```python
parser = argparse.ArgumentParser(
    prog='ProgramName',
    description='What the program does',
    epilog='Text at the bottom of help')

parser.add_argument('filename')  # positional argument
parser.add_argument('-c', '--count')  # option that takes a value
parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag

args = parser.parse_args()
print(args.filename, args.count, args.verbose)
```

## Argument groups

{meth}`add_argument_group() <argparse.ArgumentParser.add_argument_group>`

When an argument is added to the group, the parser treats it just like a normal argument, but displays the argument in a
separate group for help messages. The add_argument_group() method accepts title and description arguments which can be
used to customize this display

```pycon
>>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
>>> group1 = parser.add_argument_group('group1', 'group1 description')
>>> group1.add_argument('foo', help='foo help')
>>> group2 = parser.add_argument_group('group2', 'group2 description')
>>> group2.add_argument('--bar', help='bar help')
>>> parser.print_help()
usage: PROG [--bar BAR] foo

group1:
  group1 description

  foo    foo help

group2:
  group2 description

  --bar BAR  bar help
```

## Mutual exclusion

{meth}`add_mutually_exclusive_group() <argparse.ArgumentParser.add_mutually_exclusive_group>` create a mutually
exclusive group. argparse will make sure that only one of the arguments in the mutually exclusive group was present on
the command line

```python
parser = argparse.ArgumentParser(prog='PROG')
group = parser.add_mutually_exclusive_group()
group.add_argument('--foo', action='store_true')
group.add_argument('--bar', action='store_false')
parser.parse_args(['--foo'])
```

The {meth}`add_mutually_exclusive_group() <argparse.ArgumentParser.add_mutually_exclusive_group>` method also accepts a
required argument, to indicate that at least one of the mutually exclusive arguments is required

## Sub-commands

{meth}`add_subparsers <argparse.ArgumentParser.add_subparsers>`

Many programs split up their functionality into a number of sub-commands, for example, the svn program can invoke
sub-commands like svn checkout, svn update, and svn commit. Splitting up functionality this way can be a particularly
good idea when a program performs several different functions which require different kinds of command-line arguments.

```python
# create the top-level parser
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='sub-command help')

# create the parser for the "a" command
parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('bar', type=int, help='bar help')

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')

```

## Parser defaults

{meth}`set_defaults() <argparse.ArgumentParser.set_defaults>` allows some additional attributes that are determined
without any inspection of the command line to be added

```python
parser = argparse.ArgumentParser()
parser.add_argument('foo', type=int)
parser.set_defaults(bar=42, baz='badger')
```

{meth}`get_default() <argparse.ArgumentParser.get_default>` gets the default value for a namespace attribute, as set by
either {meth}`add_argument() <argparse.ArgumentParser.add_argument>` or by
{meth}`set_defaults() <argparse.ArgumentParser.set_defaults>`:

```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', default='badger')
parser.get_default('foo')
```

## Partial parsing

Sometimes a script may only parse a few of the command-line arguments, passing the remaining arguments on to another
script or program. In these cases, the {meth}`parse_known_args() <argparse.ArgumentParser.parse_known_args>` method can
be useful. It works much like {meth}`parse_args() <argparse.ArgumentParser.parse_args>` except
that it does not produce an error when extra arguments are present. Instead, it returns a two item tuple containing the
populated namespace and the list of remaining argument strings.

```pycon
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='store_true')
>>> parser.add_argument('bar')
>>> parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam'])
(Namespace(bar='BAR', foo=True), ['--badger', 'spam'])
```

## Intermixed parsing

{meth}`parse_intermixed_args() <argparse.ArgumentParser.parse_intermixed_args>`  
{meth}`parse_known_intermixed_args() <argparse.ArgumentParser.parse_known_intermixed_args>`

A number of Unix commands allow the user to intermix optional arguments with positional arguments.

These parsers do not support all the argparse features, and will raise exceptions if unsupported features are used. In
particular, subparsers, and mutually exclusive groups that include both optionals and positionals are not supported.

The following example shows the difference between {meth}`parse_known_args() <argparse.ArgumentParser.parse_known_args>`
and {meth}`parse_intermixed_args() <argparse.ArgumentParser.parse_intermixed_args>`: the former returns `['2', '3']` as
unparsed
arguments, while the latter collects all the positionals into rest.

```pycon
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.add_argument('cmd')
>>> parser.add_argument('rest', nargs='*', type=int)
>>> parser.parse_known_args('doit 1 --foo bar 2 3'.split())
(Namespace(cmd='doit', foo='bar', rest=[1]), ['2', '3'])
>>> parser.parse_intermixed_args('doit 1 --foo bar 2 3'.split())
Namespace(cmd='doit', foo='bar', rest=[1, 2, 3])
```

## References

- [Argparse API](inv:py3#library/argparse)
- [Argparse Tutorial](inv:py3#howto/argparse)

```{note}
There are two other modules that fulfill the same task, namely [](inv:py3#library/getopt) and the deprecated [](inv:py3#library/optparse). 
```
