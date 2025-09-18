# Handlebars Style Ruleset

Handlebars templates **MUST** be treated as backend code. All regular backend style guidelines **MUST** apply.

## 1. Spacing

Code in blocks **SHOULD** separated by lines where there is an opportunity to do so. 

```handlebars
✅ Good
<!-- START: Profile Name -->
<h3 class="profile-name">
  {{#if profile_name}}
    <span>{{profile_name}}</span>
  {{else}}
    <span>{{_ 'Guest'}}</span>
  {{/if}}
</h3>
<!-- END: Profile Name -->

❌ Bad
<!-- START: Profile Name -->
<h3 class="profile-name">
{{#if profile_name}}
<span>{{profile_name}}</span>
{{else}}
<span>{{_ 'Guest'}}</span>
{{/if}}
</h3>
<!-- END: Profile Name -->

❌ Bad
<!-- START: Profile Name -->
<h3 class="profile-name">
  <span>{{#if profile_name}}{{profile_name}}{{else}}{{_ 'Guest'}}{{/if}}</span>
</h3>
<!-- END: Profile Name -->

✅ Good
<!-- START: Profile Name -->
<h3
  class="profile-name
    {{~#if logged_in}}
      profile-logged-in
    {{~else}}
      profile-logged-out
    {{/if~}}
  "
>
  {{profile_name}}
</h3>
<!-- END: Profile Name -->

❌ Bad
<!-- START: Profile Name -->
<h3 class="profile-name{{#if logged_in}} profile-logged-in{{else}} profile-logged-out{{/if}}">
  {{profile_name}}
</h3>
<!-- END: Profile Name -->
```

- Code inside Handlebars blocks **MUST** be indented with 2 spaces.
- Code in blocks **SHOULD** be separated by blank lines where possible.
- Inline Handlebars logic (e.g., `{{#if ...}} ... {{else}} ... {{/if}}` on a single line) **MUST NOT** be used.
- Handlebars blocks and HTML structure **MUST** be formatted for readability, not compactness.

## 2. Partials

To keep HTML in the 80 character limit per line, consider using partials in order to reset the tab count.

- Partials **SHOULD** be used to keep HTML within the 80 character per line limit.
- Partials **MUST** be used to reset tab count and improve code readability.
- Large or deeply nested HTML blocks **SHOULD** be refactored into partials for reusability.
- Code duplication in HTML blocks **SHOULD NOT** occur; use partials instead.

## 3. i18n

Always consider that every product will be launched in different countries.

```handlebars
✅ Good
<h2>{{_ 'A Major Title in Example'}}</h2>

✅ Good
<h2>{{_ 'A Major %s in %s' post_title post_location}}</h2>

✅ Good
<h2>
  {{#_ 'A Major %s in %s'}}
    {{post_title}} __ {{post_location}}
  {{/_}}
</h2>

❌ Bad
<h2>Will complete in {{post_complete}} year{{#if post_complete}}s{{/if}}</h2>
```

The reason why the example above is invalid is because `year{{#if post_complete}}s{{/if}}` cannot scale to different languages.

- All user-facing text **MUST** use i18n helpers (e.g., `{{_ 'Text'}}`).
- String concatenation or inline logic for pluralization or localization (e.g., `year{{#if post_complete}}s{{/if}}`) **MUST NOT** be used.
- Templates **MUST** be written with the assumption that the product will be localized for multiple languages.
- Placeholders in i18n strings (e.g., `%s`) **SHOULD** be used for variable content.
