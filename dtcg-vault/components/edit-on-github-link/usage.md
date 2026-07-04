# When to use Edit On Github Link

Use this link to point a reader from the page they're viewing straight to that
page's source markdown on GitHub. It surfaces the substrate's open-source
posture and invites contribution — the same job GitHub's own "Edit this page"
links do on most documentation sites.

## When to use

- In the footer or margin of any content page that has a real, publicly-hosted
  markdown source (research files, component docs, foundation pages).
- Anywhere the substrate wants to signal "this content is git-tracked and
  editable by anyone," not just internally maintained.

## When not to use

- On pages generated at request time with no corresponding source file (e.g. a
  live token gallery or search-results page) — there is no markdown to edit.
- On any page whose content is customer-tenant-specific rather than part of
  the shared, public `pointsav-design-system` repository.

## Status

**Implementation deferred.** The recipe's `href` template
(`{{githubSourceUrl}}`) and the exact per-page GitHub URL construction are
specified (see Code) but not yet wired into the rendering app — an explicit
operator decision on the URL template was requested before committing it.
Treat this as a documented, ready-to-implement pattern, not a shipped one.
