## Contributing to the HyperCells & HyperBloch website

Thank you for considering contributing to the development of the HyperCells & HyperBloch website!
This document describes how to contribute to the website. If you have any questions,
please contact the maintainer.

Reading and following these guidelines will help us make the contribution process
easy and effective for everyone involved. It also communicates that you agree to
respect the time of the developers managing and developing these open source projects.
In return, we will reciprocate that respect by addressing your issue, assessing changes,
and helping you finalize your pull requests.


## Getting Started

Contributions to the HyperCells & HyperBloch website are managed through GitHub and are based on Issues
and Pull Requests. Please search for existing Issues and Pull Requests before creating
your own.

### Issues

Issues are used to track bugs, enhancements, and other requests. They are also
used as a way to discuss potential changes before opening a Pull Request.
If possible, please use one of the templates provided when creating a new Issue,
filling in as much information as possible, and adding the appropriate labels.

If you find an existing Issue that addresses your concern, please add a comment
with your own reproduction steps to the existing Issue rather than creating a new
one. This helps us focus on the discussion in one place rather than having to track
multiple Issues.

### Pull Requests

Pull Requests are used to propose changes to the codebase. They are also used
to propose changes to the documentation. Please follow the guidelines below when
creating a Pull Request.

- Discuss your proposal first before creating a Pull Request by opening an Issue
  or by contacting the maintainer. This helps us understand your proposal and make
  sure it is something that will be accepted.
- If your Pull Request is related to an existing Issue, please reference the Issue
  in the description of your Pull Request.
- Add unit tests for fixed or changed functionality.
- Update the documentation as needed.
- Please use the following scheme for branch names:
  ```
  <category>/<reference>/<branch name>
  ```
  where `<category>` is one of the following:
    - `feat`: new feature
    - `bugfix`: bug fix
    - `hotfix`: hot fix
  and `<reference>` is a reference to an issue (or no-ref if there is no reference),
  and `<branch name>` is a short but descriptive name.
- Please use the following scheme for commit messages:
  ```
  <category>: first thing; second thing
  ```
  where `<category>` is one of the following:
  - `feat`: new feature
  - `fix`: bug fix
  - `refactor`: code change that neither fixes a bug nor adds a feature
  - `chore`: writing documentation or adding tests (not related to a new feature or change), changing formatting, etc.

In general, we follow the <a target="_blank" href="https://github.com/susam/gitpr">"fork-and-pull" Git workflow</a>
1. Fork the repository to your own Github account
2. Clone the project to your machine
3. Create a branch locally (see above for naming conventions)
4. Commit changes to the branch (see above for commit message conventions)
5. Push changes to your fork
6. Open a Pull Request in our repository

## Style guide

Please follow the following style guide when contributing to existing pages or creating new pages. 

- Page with subpages (including further nested pages): 

  Use a restructured text file  (.rst) for the page in the lowest level followed either by a markdown 
  (.md) or .rst files as subpages. 
  - Primary sidebar (left):

    Make sure that the primary sidebar (left sidebar) is displayed, if not, you may need 
    to modify the conf.py file and delete the corresponding page from the list `html_sidebars`.
  - Secondary sidebar (right):

    If you disable the secondary sidebar via:

    ````{tab-set-code}
    ```{code-block} rst
    
    :html_theme.sidebar_secondary.remove: true
    ```

    ```{code-block} markdown

    ---
    html_theme.sidebar_secondary.remove: true
    ---
    ```
    ````

    make sure you include the following code snippet in the corresponding files, 
    in order to appropriately adjust the width and alignment of the elements in the page:

    ````{tab-set-code}
    ```{code-block} rst
    .. raw:: html
    <style type="text/css">
      @media (min-width: 959.98px) {
        .bd-main .bd-content {
          max-width: 80%!important; 
          text-align:left!important;
        }
      }
    </style>
    ```

    ```{code-block} markdown
    <style type="text/css">
      @media (min-width: 959.98px) {
        .bd-main .bd-content {
          max-width: 80%!important; 
          text-align:left!important;
        }
      }
    </style>
    ```
    ````

- Page without subpages: 

  - Primary sidebar (left):

    If there are no subpages disable the primary sidebar by modifying
    the conf.py file,  as follows:
    ```python
    html_sidebars = { 
	    # ... other pages here
	    "<relative path to page>/pagename" : []
    ```
  - Secondary sidebar (right):
  
    If you **include** a secondary sidebar, make sure to appropriately adjust the width and alignment 
    of the elements in the page by including the following code snippet in the corresponding file:

    ````{tab-set-code}
    ```{code-block} rst
    .. raw:: html
      <style type="text/css">
        @media (min-width: 959.98px) {
          .bd-main .bd-content  {
            max-width: 84.1%;
            align-self: end;
          }
          .bd-main .bd-content .bd-sidebar-secondary .bd-toc {
            align-items:right;
          }
        }
      </style>
    ```

    ```{code-block} markdown
    <style type="text/css">
      @media (min-width: 959.98px) {
        .bd-main .bd-content  {
          max-width: 84.1%;
          align-self: end;
        }
        .bd-main .bd-content .bd-sidebar-secondary .bd-toc {
          align-items:right;
        }
      }
    </style>
    ```
    ````

    otherwise, **disable** the secondary sidebar as follows:

    ````{tab-set-code}
    ```{code-block} rst
 
    :html_theme.sidebar_secondary.remove: true
    ```

    ```{code-block} markdown

    ---
    html_theme.sidebar_secondary.remove: true
    ---
    ```
    ````

## License

By contributing, you agree that your contributions will be licensed under the below
mentioned licenses.
Contributions to tutorial code, i.e., code examples downloadable as source files and
code provided in the tutorials, will be licensed under the [CC0 1.0 License](license_code.txt),
while any other contribution to the website will be licensed under the CC BY-SA-4.0 License,
as described in the [LICENSE](LICENSE.txt) file.

## References

Parts of this document are based on the template provided by [Auth0](https://github.com/auth0):
[https://github.com/auth0/open-source-template/blob/master/GENERAL-CONTRIBUTING.md]