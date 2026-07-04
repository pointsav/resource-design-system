---
title: Code Block With Copy — Code
---

# Code

## Dependencies

- Primitives: color, spacing
- Assets: none
- JS binding: `data-ps-copy` attribute on the copy button

## HTML + CSS recipe

```html
<div class="ps-code-block">
  <pre><code>{{content}}</code></pre>
  <button type="button" class="ps-code-block__copy" data-ps-copy aria-label="Copy to clipboard">Copy</button>
</div>
```

## Copy interaction

`navigator.clipboard.writeText` is the primary path, with a `<textarea>` +
`document.execCommand('copy')` fallback for restricted contexts where the
Clipboard API isn't available:

```js
document.querySelectorAll('[data-ps-copy]').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var code = btn.previousElementSibling.textContent;
    var onCopied = function () {
      var prevLabel = btn.getAttribute('aria-label');
      btn.textContent = 'Copied';
      btn.setAttribute('aria-label', 'Copied to clipboard');
      setTimeout(function () {
        btn.textContent = 'Copy';
        btn.setAttribute('aria-label', prevLabel);
      }, 1400);
    };
    if (navigator.clipboard) {
      navigator.clipboard.writeText(code).then(onCopied);
    } else {
      var ta = document.createElement('textarea');
      ta.value = code;
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
      onCopied();
    }
  });
});
```

A working reference implementation of this exact pattern ships live in this
substrate's own CMS (`app-privategit-design/static/code-copy.js`), wired to
every rendered `<pre>` block on this site.
