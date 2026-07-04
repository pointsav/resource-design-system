# When to use Empty State Card

Use an empty state card for any surface that legitimately has no data yet —
an index page with no entries, a dashboard panel awaiting its first data
point, or a search result with no matches. A dashed border and a short
title + body pair signal "this is empty by design," not "this is broken."

## When to use

- Index/listing pages before any items have been created.
- Dashboard panels or widgets waiting on their first data point.
- Search or filter results that legitimately return zero matches.

## When not to use

- Loading states — use a skeleton or spinner instead; an empty state
  implies "there is nothing here," which is misleading mid-fetch.
- Error states — a failed request is not the same as an empty result;
  use a [Notification](/components/notification/usage/) instead so the
  user knows to retry rather than assuming there's simply no data.
- Permanently-empty decorative sections — if a section will never have
  content, remove the section rather than showing an empty state for it.

## Content

Title uses the display-serif face; body uses the body-sans face. Optional
inline links are separated by whitespace, not bullets, since they read as
next steps ("Create your first record" · "Learn more") rather than a list
of options.
