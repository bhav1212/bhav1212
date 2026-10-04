#!/usr/bin/env python3
"""Create a self-hosted GitHub contribution graphic from the actual API calendar."""
from pathlib import Path
from html import escape
from urllib.request import Request, urlopen
import argparse, json, os

ROOT = Path(__file__).resolve().parents[1]
QUERY = 'query { user(login: "bhav1212") { contributionsCollection { contributionCalendar { totalContributions weeks { contributionDays { date contributionCount weekday } } } } } }'


def render(calendar):
    weeks = calendar['weeks']
    days = [day for week in weeks for day in week['contributionDays']]
    assert days and len(weeks) <= 54, 'Expected a one-year GitHub calendar'
    assert all(day['contributionCount'] >= 0 and 0 <= day['weekday'] <= 6 for day in days)
    maximum = max(day['contributionCount'] for day in days) or 1
    colors = ['#1b2730', '#1f4c44', '#276e60', '#399d86', '#79cdb8']
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 208" width="1000" height="208" role="img" aria-labelledby="title desc">',
           '<title id="title">Bhavesh Jain — GitHub contribution activity</title>',
           f'<desc id="desc">{calendar["totalContributions"]} GitHub-reported contributions from {days[0]["date"]} to {days[-1]["date"]}. Updated weekly.</desc>',
           '<style>text{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}.scan{animation:scan 12s linear infinite}@keyframes scan{from{transform:translateX(0)}to{transform:translateX(822px)}}@media(prefers-reduced-motion:reduce){.scan{animation:none;display:none}}</style>',
           '<rect width="1000" height="208" rx="14" fill="#0d1117"/>',
           '<text x="30" y="31" fill="#e6edf3" font-size="17">GitHub activity</text>',
           f'<text x="970" y="31" text-anchor="end" fill="#79cdb8" font-size="14">{calendar["totalContributions"]} contributions</text>',
           '<defs><clipPath id="calendar"><rect x="82" y="53" width="822" height="101"/></clipPath></defs>']
    for label, weekday in [('Mon', 1), ('Wed', 3), ('Fri', 5)]:
        svg.append(f'<text x="30" y="{65 + weekday * 14}" font-size="10" fill="#a6b3c2">{label}</text>')
    for index, week in enumerate(weeks):
        for day in week['contributionDays']:
            count = day['contributionCount']
            level = 0 if count == 0 else min(4, 1 + int((count / maximum) ** .5 * 3))
            svg.append(f'<rect x="{82 + index * 15}" y="{53 + day["weekday"] * 14}" width="11" height="11" rx="2" fill="{colors[level]}"><title>{escape(day["date"])}: {count} contributions</title></rect>')
    svg += ['<g clip-path="url(#calendar)"><rect class="scan" x="66" y="53" width="2" height="99" fill="#c6f3e5" opacity=".6"/></g>',
            f'<text x="30" y="184" font-size="11" fill="#a6b3c2">Snapshot · {days[0]["date"]} → {days[-1]["date"]}</text>',
            '<text x="970" y="184" text-anchor="end" font-size="11" fill="#a6b3c2">GitHub API · updated weekly</text>', '</svg>']
    return '\n'.join(svg) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, help='Saved GraphQL response for reproducible local generation')
    args = parser.parse_args()
    if args.input:
        payload = json.loads(args.input.read_text())
    else:
        token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
        if not token:
            raise SystemExit('Set GH_TOKEN or GITHUB_TOKEN; the token is never written to the asset.')
        request = Request('https://api.github.com/graphql', data=json.dumps({'query': QUERY}).encode(), headers={'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json', 'User-Agent': 'bhav1212-profile'})
        with urlopen(request, timeout=30) as response:
            payload = json.load(response)
    if payload.get('errors'):
        raise SystemExit('GitHub returned a GraphQL error; keeping the last valid activity graphic.')
    calendar = payload['data']['user']['contributionsCollection']['contributionCalendar']
    output = ROOT / 'assets/contribution-calendar.svg'
    output.parent.mkdir(exist_ok=True)
    output.write_text(render(calendar))
    print(f'Updated {output.name} from GitHub calendar data.')


if __name__ == '__main__':
    main()
