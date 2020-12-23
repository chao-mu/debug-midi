# debug-midi
Debug midi controllers

## Please Note!

Mido (the midi library this is based on) currently strips driver-level timestamps. The timestamps you see are printed out from python.  

## Usage - Examples

Display general help (subcommands also support --help)
```
$ ./debug-midi.py  --help
usage: debug-midi.py [-h] {list,dump} ...

Debug midi devices

positional arguments:
  {list,dump}  commands
    list       List midi ports
    dump       dump midi messages

optional arguments:
  -h, --help   show this help message and exit
```

List available ports
```
$ ./debug-midi.py  list
Input Ports (readable)
    Launchkey MK3 49:Launchkey MK3 49 MIDI 1 20:0
    Launchkey MK3 49:Launchkey MK3 49 MIDI 2 20:1
    Midi Through:Midi Through Port-0 14:0

Output Ports (writable)
    Launchkey MK3 49:Launchkey MK3 49 MIDI 1 20:0
    Launchkey MK3 49:Launchkey MK3 49 MIDI 2 20:1
    Midi Through:Midi Through Port-0 14:0
```

Dump midi messages, skipping clock messages
```
$ python debug-midi.py dump --name 'Launchkey MK3 49:Launchkey MK3 49 MIDI 1 20:0' --skip-clock
Listening on 'Launchkey MK3 49:Launchkey MK3 49 MIDI 1 20:0'. ctrl-c to exit
1608744990.4160621 <message note_on channel=0 note=43 velocity=51 time=0>
1608744990.5404718 <message note_on channel=0 note=43 velocity=0 time=0>
```

