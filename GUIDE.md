# Pizza 24 TV Menu Guide

## 1. Create the Google Sheet

Create one Google Sheet with exactly these 3 tabs:

- `menu`
- `promos`
- `settings`

Use the seed files in [`sheet-seed`](/Users/one.6ix/Documents/New%20project/pizza24/sheet-seed) and keep the headers exactly the same.

### `menu` tab columns

`active, category, item_name, size, price, description, badge, sort_order`

### `promos` tab columns

`active, title, subtitle, price_text, code, details, sort_order`

### `settings` tab columns

`key, value`

## 2. Fill the sheet

The current Pizza 24 Kamloops menu and deals have already been extracted into:

- [menu.csv](/Users/one.6ix/Documents/New%20project/pizza24/sheet-seed/menu.csv)
- [promos.csv](/Users/one.6ix/Documents/New%20project/pizza24/sheet-seed/promos.csv)
- [settings.csv](/Users/one.6ix/Documents/New%20project/pizza24/sheet-seed/settings.csv)

Fastest path:

1. Create the three tabs.
2. Open each CSV locally.
3. Copy everything into the matching Google Sheet tab.

## 3. Publish the sheet

In Google Sheets:

1. Open `File`
2. Choose `Share`
3. Choose `Publish to web`
4. Publish the whole document one time

## 4. Copy the Sheet ID

Example URL:

`https://docs.google.com/spreadsheets/d/1AbCdEfGhIjKlMnOpQrStUvWxYz1234567890/edit#gid=0`

The Sheet ID is the part between `/d/` and `/edit`:

`1AbCdEfGhIjKlMnOpQrStUvWxYz1234567890`

## 5. Edit one line in `display.html`

Open [display.html](/Users/one.6ix/Documents/New%20project/pizza24/display.html) and replace:

```js
const SHEET_ID = "PASTE_YOUR_GOOGLE_SHEET_ID_HERE";
```

with your real Sheet ID.

## 6. Upload to GitHub Pages

Use this repo as a static site:

1. Push the repo to GitHub.
2. In GitHub, open `Settings` for the repo.
3. Open `Pages`.
4. Set source to deploy from the main branch root.
5. Save.

Your permanent URL will look like:

`https://YOUR-USERNAME.github.io/pizza24/`

## 7. Open it on each TV

Open the GitHub Pages URL in the TV browser, or Silk Browser on Fire Stick.

The page refreshes from Google Sheets every 60 seconds, so future menu and promo changes only need Sheet edits.

## Notes

- Source used for menu extraction: [Pizza 24 Kamloops menu](https://www.pizza24kamloops.ca/menu)
- Source used for homepage promos: [Pizza 24 Kamloops home page](https://www.pizza24kamloops.ca/)
- The homepage also shows promo codes that may be time-limited, so review the `promos` tab before publishing.
