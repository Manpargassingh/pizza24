#!/usr/bin/env python3
"""Extract the current Pizza 24 Kamloops menu into CSV seed rows."""

from __future__ import annotations

import csv
import html
import io
import re
import urllib.request

MENU_URL = "https://www.pizza24kamloops.ca/menu"


def main() -> None:
    source = urllib.request.urlopen(MENU_URL).read().decode("utf-8", "ignore")
    sections = [
        (match.start(), clean(match.group(1)))
        for match in re.finditer(r'data-hook="section.name"[^>]*>(.*?)</span>', source)
    ]
    sections.append((len(source), None))

    rows: list[list[str]] = []
    sort_order = 10

    for index in range(len(sections) - 1):
      start, section_name = sections[index]
      end = sections[index + 1][0]
      section_html = source[start:end]

      for match in re.finditer(
          r'<div data-hook="item.container".*?(?=<div class="sF5Sps0" role="listitem"|</script>|$)',
          section_html,
          re.S,
      ):
          item_html = match.group(0)
          item_name_match = re.search(r'data-hook="item.name">(.*?)</span>', item_html, re.S)
          if not item_name_match:
              continue

          item_name = clean(item_name_match.group(1))
          desc_match = re.search(r'data-hook="item.description">(.*?)</span>', item_html, re.S)
          description = clean(desc_match.group(1)) if desc_match else ""

          variants = re.findall(
              r'data-hook="variant.name">(.*?)</span>.*?data-hook="variant.price">(.*?)</span>',
              item_html,
              re.S,
          )
          if variants:
              for size, price in variants:
                  rows.append(
                      [
                          "TRUE",
                          section_name or "MENU",
                          item_name,
                          clean(size),
                          clean(price),
                          description,
                          "",
                          str(sort_order),
                      ]
                  )
                  sort_order += 10
              continue

          price_match = re.search(r'data-hook="item.price">(.*?)</span>', item_html, re.S)
          price = clean(price_match.group(1)) if price_match else ""
          rows.append(
              [
                  "TRUE",
                  section_name or "MENU",
                  item_name,
                  "",
                  price,
                  description,
                  "",
                  str(sort_order),
              ]
          )
          sort_order += 10

    # These two rows are present in the live menu page but sit at the page tail.
    rows.extend(
        [
            [
                "TRUE",
                "NACHOS",
                "Nachos",
                "Regular",
                "$10.99",
                "Cheesy, crispy, spicy, loaded nachos with green peppers, olives, ring onion, jalapeno peppers, double cheese melt, optional chicken or beef.",
                "",
                str(sort_order),
            ],
            [
                "TRUE",
                "NACHOS",
                "Large Nachos",
                "Large",
                "$19.99",
                "Cheesy, crispy, spicy, loaded nachos with green peppers, olives, ring onion, jalapeno peppers, double cheese melt, optional chicken or beef.",
                "",
                str(sort_order + 10),
            ],
        ]
    )

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(
        ["active", "category", "item_name", "size", "price", "description", "badge", "sort_order"]
    )
    writer.writerows(rows)
    print(output.getvalue(), end="")


def clean(value: str) -> str:
    text = re.sub(r"<.*?>", "", value)
    return " ".join(html.unescape(text).split())


if __name__ == "__main__":
    main()
