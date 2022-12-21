# Module systems for JavaScript

# ECMAScript 6 / ES2015 Modules

https://2ality.com/2014/09/es6-modules-final.html

The goal for ECMAScript 6 modules was to create a format that both users of CommonJS and of AMD are happy with:

- Similar to CommonJS, they have a compact syntax, a preference for single exports and support for cyclic dependencies.
- Similar to AMD, they have direct support for asynchronous loading and configurable module loading.
- Being built into the language allows ES6 modules to go beyond CommonJS and AMD (details are explained later):

- Their syntax is even more compact than CommonJS’s.
- Their structure can be statically analyzed (for static checking, optimization, etc.).
- Their support for cyclic dependencies is better than CommonJS’s.

The ES6 module standard has two parts:

- Declarative syntax (for importing and exporting)
- Programmatic loader API: to configure how modules are loaded and to conditionally load modules

# CommonJS Modules

The dominant implementation of this standard is in Node.js (Node.js modules have a few features that go beyond CommonJS). Characteristics:

- Compact syntax
- Designed for synchronous loading
- Main use: server

# Asynchronous Module Definition (AMD)

The most popular implementation of this standard is RequireJS. Characteristics:

- Slightly more complicated syntax, enabling AMD to work without eval() (or a compilation step).
- Designed for asynchronous loading
- Main use: browsers
