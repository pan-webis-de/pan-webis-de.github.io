# Portraits for PAN organizers and speakers

Put portraits of people who appear on the PAN pages here. External organizers can add them directly in this repository; the central image store (`webis-de-assets`) stays with Webis.

| File               | Content                           |
|--------------------|-----------------------------------|
| `<key>.jpg`        | thumbnail, exactly 105×140 px     |
| `master/<key>.jpg` | same crop, 210×280 to 840×1120 px |

**File name:** `<key>` is the person's last name in lowercase ASCII, e.g. `goedel.jpg`. If that name is already taken by someone else, here or in the central store ([people](https://github.com/webis-de/webis-de-assets/tree/master/img/people), [event-people](https://github.com/webis-de/webis-de-assets/tree/master/img/event-people)), append the first name: `goedel-kurt.jpg`. Thumbnail and master use the same name.

Full format and naming: [Target format](https://github.com/webis-de/webis-de-assets/blob/master/_maintenance/README-crop-portraits.md#target-format). On a Mac, the script [`crop-portraits.py`](https://github.com/webis-de/webis-de-assets/blob/master/_maintenance/crop-portraits.py) produces both files from any photo: its `105x140/<key>.jpg` goes here, its `master/<key>.jpg` into `master/`.

`example.jpg` and `master/example.jpg` are a drawn placeholder that shows size and head position; copy their framing, keep them, and leave them out of the yearly move.

Use the thumbnail in a people card:

```html
<img src="{{ '/img/event-people/<key>.jpg' | relative_url }}" alt="<Full Name>">
```

Once a year, Webis moves these files to `webis-de-assets/img/event-people/` (same layout) and points the cards to `https://assets.webis.de/img/event-people/<key>.jpg`.
