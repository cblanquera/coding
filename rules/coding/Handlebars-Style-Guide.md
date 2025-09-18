#  Handlebars

At all times Handlebars should be treated as backend code, thus all regular backend style guidelines should apply.


## 1. Spacing

Code in blocks should separated by lines where there is an opportunity to do so. Code inside of Handlebar blocks should be indented with 4 spaces.

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

## 2. Partials

To keep HTML in the 80 character limit per line, consider using partials in order to reset the tab count.

```handlebars
❌ Bad
<div class="post-search-body post-{{type}}" >
  {{#unless profile_banner}}
    <form action="/post/search" class="post-search-form">
      <div class="search-group">
        <div
          class="tag-field"
          data-do="tag-field"
          data-name="q"
          data-suggest=true
        >
          {{#each q}}
            <div class="tag bordered">
              <input
                autocomplete="off"
                class="tag-input text-field"
                data-do="suggestion-field"  
                name="q[]"
                placeholder="{{_ 'Enter Search'}}"
                type="text"
                value="{{this}}"
              />
              <a class="remove" href="javascript:void(0)">x</a>
            </div>
          {{/each}}
          {{#if type}}
            <input name="type" type="hidden" value="{{type}}">
          {{/if}}
          <div class="pull-right search-icon">
            <button type="submit">
              <i class="fa fa-search" aria-hidden="true"></i>
            </button>
          </div>
        </div>
        <div class="text-blue">Suggested Filters:</div>
        <div class="suggested-terms">
          {{#each terms}}
          <a
            class="btn btn-white"
            data-do="add-keyword"
            data-on="click"
            data-value="{{term_name}}"
          >
            {{term_name}}
          </a>
          {{/each}}
        </div>
      </div>
    </form>
  {{/unless}}
</div>

✅ Good
<div class="post-search-body post-{{type}}" >
  {{#unless profile_banner}}
    <form action="/post/search" class="post-search-form" >
      {{> search_fields}}
    </form>
  {{/unless}}
</div>
```

Use partials to keep the HTML code as small as possible while providing reusability on HTML code blocks.


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