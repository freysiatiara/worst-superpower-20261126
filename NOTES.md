# Worst Superpower — build notes

- Bounty: Worst Superpower — https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe
- Slug: `u-suroto-worst-superpower-461dcdbe`
- Pot: $2, winner-take-all (only rank 1 paid). Entry fee $0.00.
- Deadline: 2026-11-26T17:30:00Z (2026-11-27 00:30 WIB).
- Blind, 3 rounds. Round 1 cutoff: 2026-11-26T01:30:26Z (2026-11-26 08:30 WIB).
- Task: one line, max 140 characters, inventing the most useless superpower.
  Judge (Bradley-Terry pairwise) weighs, in order: (1) genuinely useless in one
  line, (2) uselessness lands as a joke you can picture in use, (3) unexpected
  (not a familiar gag), (4) tight wording + concrete detail, (5) clear on one
  reading. Tie-break: fewer bytes, then earlier receipt. Target: 90–120 chars.
- Field at build time: 561 entries.

## Field clusters avoided (saturated)

stop-time-one-second-already-used, teleport-to-where-I'm-standing,
damp-left-sock, goldfish-castle, green-lights-behind-me,
rain-one-drop-on-my-head, predict-yesterday, read-my-own-mind,
count-rice-after-eating, breathe-underwater-in-bath,
summon-what-I-already-hold, turn-water-into-water, frozen-fish-talking,
password-memory, queue-moves-faster, pigeon-minds, houseplant-minds,
invisible-when-nobody-looks, rewind-costs-more, teleport-3cm,
microwave-beep, fitted-sheet-folding, traffic-lights-behind-me,
lie-detector-too-late, paper-cuts-left-thumb,
find-second-sock-after-replacement, door-never-locked.
Many entries are also just titled "Worst Superpower" with no line at all.

## Candidate panel (character counts verified by script)

| # | Candidate | Chars | Bytes |
|---|-----------|------:|------:|
| P1 | I can make any light bulb last forever — but only by never turning it on, so my superpower is sitting in the dark. | 114 | 116 |
| P2 | I can turn any Monday into a Friday — but only by sleeping through the week, which HR calls unauthorised leave. | 111 | 113 |
| P3 | I can find any lost TV remote — but only by sitting on it, which is exactly how it got lost. | 92 | 94 |
| P4 | I can put any song in your head — but only the one already stuck in mine, so my power is just humming badly. | 108 | 110 |
| P5 | I can finish any book in seconds — but only books I've already finished, so my superpower is just rereading faster than I read. | 127 | 129 |
| P6 | I can stop any baby crying — but only by crying louder, and the baby has filed a complaint. | 91 | 93 |
| P7 | I can charge any phone to 100% just by thinking about it — but only while it's already at 100%. | 95 | 97 |
| M1 | I can see through any wall — but only walls made of glass, which everyone else just calls windows. | 98 | 100 |
| M2 | I can control the weather — but only indoors, where the thermostat was already doing it better than me. | 103 | 105 |
| M3 | I can travel through time — but only forwards, at one second per second, exactly like everyone else. | 100 | 102 |
| M4 | I can win any lottery — but only ones I never entered, so my prize is a ticket I do not own. | 92 | 94 |
| M5 | I can make any food taste better — but only by adding salt, which is just cooking badly with confidence. | 104 | 106 |
| M6 | I can stop bullets with my mind — but only bullets in a museum, which nobody was about to fire. | 95 | 97 |
| M7 | I can make any elevator arrive instantly — but only by pressing the button, which is what the button is for. | 108 | 110 |
| M8 | I can speak every language fluently — but only to people who already speak mine, so my power is just nodding. | 109 | 111 |
| M9 | I can summon lightning on demand — but only during thunderstorms, when the sky was doing it anyway. | 99 | 101 |
| M10 | I can heal any injury instantly — but only injuries I do not have yet, so my power is just worrying early. | 106 | 108 |

P5 is 127 chars — outside the 90–120 target, so it loses on criterion 4
(tightness) before the head-to-head. M3 is a known internet gag ("time travel
forwards at normal speed"), so it loses on criterion 3 (unexpected).

## Head-to-head (finalists: P1, P3, P7, M1)

- M1 vs P1: both absolutely useless; M1's reframe lands instantly (glass wall
  = window) while P1's payoff ("sitting in the dark") arrives slower; M1 is
  tighter (98 vs 114 chars, 100 vs 116 bytes) — tie-break advantage. M1 wins.
- M1 vs P3: P3 is shorter (92 chars) and its circular joke is relatable, but
  "sitting on the remote" is a familiar domestic image, while M1's twist is
  more surprising. M1 wins on criterion 3.
- M1 vs P7: P7 is a clean paradox but its picture is weak (thinking at a phone
  already at 100% is hard to visualise); M1 wins on criterion 2.
- M6, M4, M9, M2, M10, M5, M7, M8, P2, P4, P6 are all solid two-beat lines but
  lose to M1 on at least one of: picture vividness (M6, M9), surprise (M7, M8),
  or tightness (P2, P4).

## Winner

> I can see through any wall — but only walls made of glass, which everyone else just calls windows.

98 characters, 100 bytes. X-ray vision with a catch that deletes it: the only
walls it works on are glass, which is just looking through a window — a
superpower everyone already has. Uselessness is absolute (criterion 1), the
picture is instant (criterion 2), the glass-wall twist is fresh (criterion 3),
the wording is tight with a concrete detail (criterion 4), and it reads clear
in one pass (criterion 5). No saturated cluster touched.

## Run

```sh
python3 main.py   # writes /output/entry.txt, mode 0644, stdlib only
```
