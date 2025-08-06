# Question: Web Application Design with Nuxt and NuxtUI

We are currently updating our in-house WebApp from Vue.js 2 to Vue 3. We hope to complete this in 3 months time.
As part of this, we have decided to use Nuxt as the framework for the site, including the NuxtUI component library.

1. Starting from this point, please describe your approach to the following design:

> A single-page application featuring a Navigation Sidebar with a Site Menu; a Header with a User Avatar and Menu; all surrounding the main content.

```{note}
For this exercise, we are not concerned with code, but rather what considerations you would have for the design based on the information about the listed resources. Give some examples of how you would structure such an application.
```

## Answer

### Considerations

#### Site Improvements
Why are we upgrading to Vue3 and using the NuxtUI component library, does this actively solve any headaches we've had when devloping in the past?
- Need to identify the parts of the codebase that are made easier by updating frameworks to leverage the improvements
- What are previous complaints with the site how can these be improved?

#### Hosting
Are we going to host on a cloud service and make use of distribution, does content differ between users in a way that would affect page caching in a CDN?
Is this app going to be exposed publicly, what should not be indexed by google?

#### Security
General security considerations include:
- How to manage certificates.
- What interactions are taking place over the browser? If transactions happen from the browser ideally need to use temporary keys such as OAUTH2 tokens.
- User Agent implies that there is login functionality. How are login credentials being stored? Passwords should be encrypted on the database.
- Ensure that any data access over the browser does not expose and form of query language. Ideally this should be abstracted out and data access queries should be formed server side.
- Content-security policy should be added to limit potential for XSS with the addition of random nonce tokens generated server-side for any inline scripts

#### Integrations
What third-part tools need to be integrated with, this might include:
- Backend CMS
  - How is content going to be retireved from the CMS, headless API?
- Third party web service
  - Inegrate with API/RSS feed for data, what authentication is required for this. Refer to security considerations.
  - Is content being loaded on the page directly from these sites? These need to be included in the CSP.


### Design
####Reusable Components
There a 3 separate components defined here which should be reusable across all pages:
- Navigation Sidebar
- Header
- User Avatar
- Menu

#### Structure
Following the standard nuxt structure, the structure of the code under src would look something like:
```
project-root/
├── assets/          # Uncompiled assets like SCSS, images, fonts
├── components/      # Reusable Vue components
│   ├── Sidebar.vue
│   ├── Header.vue
│   ├── UserAvatar.vue
│   └── MenuDropdown.vue
├── composables/     # Reusable stateless js functions
├── layouts/         # App layout templates
│   └── default.vue  # Default layout containing sidebar and header
├── middleware/      # Route guards and logic before page loads
├── pages/           # Route-based page views
│   └── home 
│   │   └── index.vue 
├── plugins/         # Client/server plugins
├── public/          # Static files
├── app.vue          # Root component, wraps all the layouts/pages
├── nuxt.config.ts   # Nuxt configuration file
└── .nuxt/           # Auto-generated build files (ignored in version control)
```
The header would import the **UserAvatar** and **MenuDropdown** components while the **Sidebar** and **Header** would be used in the default layout which is then leveraged by all files under pages/

Routing for pages is handled automatically

### Benefits of Nuxt
Some benefits of Nuxt:
- Routing handled automatically by structure under 'pages' folder
- Only js required for the requested page is sent to the browser, improving load times
- Reusable layouts
- Ability to write content in markdown. Makes addition of content writers easier.
- Useful built-in composables for things such as data fetching, state management, and metadata.
- Useful built-in page-transition component