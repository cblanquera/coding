# Coding Standards

My Coding Standards. Before contributing to anyone's code, be sure to study how the existing project code 
is expressed. It's important that all code in a project closely matches each others.

> ❌ Do not use your own standards irrespective of the existing project's code. Even if they have not
> explicitly set a standard.

## Char Length

Code should be written like a book. A book has pages and each line of each page has a common max length.
Imagine a child's eye moving from left to right when reading a book. As that child reads while growing 
up, their eyes move a lot less. Eventually a person moves from letter to letter, to word by word, to line 
by line, and some can even do page by page *(speed reading)*. This is because as a person reads more and 
more they develop their sight peripherals, but there is a limit to how far peripherals can reach *(less 
than 180 degrees)*. Around when an individual's sight peripherals reach their limit is when the eyes need 
to move. Eyes moving constantly without rest can cause eye stress. Unlike a book, there is no max length 
a line of code could be and contributes to eye stress for everyone reading code not having a standard.

> Every line of code should not exceed **80 characters**.

If you are using VSCode 
 1. Go to File > Preferences > Settings.
 2. Search for "rulers"
 3. Click "Edit in settings.json"
 4. Add the following to `settings.json`

```js
"editor.rulers": [ 72, 80, 100, 120 ],
```

## Tabbing

In all circumstances use **2 spaces** for tabbing.

 - Do not use 4 spaces for tabbing
 - Do not use *[tab]* for tabbing

## Quotes

By default, prefer single quotes (**'**) over double quotes (").

 - Use template quotes (`) for templating use or for quotes with multiple lines.
 - Use double quotes for HTML and React attributes

## Variable Naming

Variable names should be camelCased. When choosing a name please make the following considerations.

 - use nouns
 - Variables representing booleans, can use `is` or `valid`
 - Variables representing functions, follow function naming
 - Variables representing class definitions, follow class naming

