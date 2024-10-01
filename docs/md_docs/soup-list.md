# SOUP List (Software of Unknown Provenance)

> The 62304 requires you to document your SOUP, which is short for Software of Unknown Provenance. In human
> language, those are the third-party libraries you're using in your code, typically in your
> `requirements.txt` or `Gemfile`.

| Classes | IEC 62304:2006 Section                          | Document Section |
|---------|-------------------------------------------------|------------------|
| B, C    | 5.3.3 (Functional and Performance Requirements) | 2                |
| B, C    | 5.3.4 (Hardware and Software Requirements)      | 2                |
| B, C    | 7.1.2 (Hazardous Situations)                    | 2                |
| B, C    | 7.1.3 (SOUP Anomaly Lists)                      | 2                |
| A, B, C | 8.1.2 (Identify SOUP)                           | 2                |

## 1 Risk Level Definitions

> The 62304 requires you to assess risks associated with SOUP. The simplest way to do this is to classify each
> SOUP as a certain risk level. Unless you're developing software which shoots radiation at patients, it's
> likely that your SOUP risk levels remain "low" or "medium".

| Risk Level | Definition                                                 |
|------------|------------------------------------------------------------|
| Low        | Malfunction in SOUP can't lead to patient harm.            |
| Medium     | Malfunction in SOUP can lead to reversible patient harm.   |
| High       | Malfunction in SOUP can lead to irreversible patient harm. |

## 2 SOUP List

> This is the actual SOUP list. For each third-party library you use, add an entry in the table below. The
> idea is to only have one "global" SOUP list for your medical device even though the code may actually live
> in multiple repositories. That's what the "software system" column is for; you could also mention your (git)
> repository there.

> When specifying requirements, the 62304 requires you to mention functional, performance, hard- and software
> requirements. However, you may not have to re-state certain requirements if they apply to all SOUP,
> e.g., "runs on Linux". So prefer to keep the requirements simple, in a way in which you would communicate them
> to colleagues on your development team when answering the question "why did we import this library?".

> As with all templates: It's more about the content (i.e., the columns you see below) than the tool (filling
> this out in Google sheets / markdown / wherever). Nobody says that you have to maintain this as a Google
> sheet. If you can find a way to integrate this in your workflow in a better way, e.g., in a markdown file in
> your git repository, go for it! Just keep in mind that you need to be able to export it to send it to
> auditors.

| ID | Software System | Package Name | Programming Language | Version | Website                                          | Last verified at | Risk Level | Requirements               | Verification Reasoning                                                    |
|----|-----------------|--------------|----------------------|---------|--------------------------------------------------|------------------|------------|----------------------------|---------------------------------------------------------------------------|
| 1 | Unknown | certifi | Python | 2024.8.30 | [https://github.com/certifi/python-certifi](https://github.com/certifi/python-certifi) | 2024-08-30 | N/A | N/A | N/A |
| 2 | OS Independent | charset-normalizer | Python | 3.3.2 | [https://github.com/Ousret/charset_normalizer](https://github.com/Ousret/charset_normalizer) | 2023-11-01 | N/A | N/A | N/A |
| 3 | Unknown | contourpy | Python | 1.3.0 | [unknown](unknown) | 2024-08-27 | N/A | N/A | N/A |
| 4 | Unknown | cycler | Python | 0.12.1 | [unknown](unknown) | 2023-10-07 | N/A | N/A | N/A |
| 5 | OS Independent | fonttools | Python | 4.54.1 | [http://github.com/fonttools/fonttools](http://github.com/fonttools/fonttools) | 2024-09-24 | N/A | N/A | N/A |
| 6 | OS Independent | idna | Python | 3.10 | [unknown](unknown) | 2024-09-15 | N/A | N/A | N/A |
| 7 | Unknown | importlib_resources | Python | 6.4.5 | [unknown](unknown) | 2024-09-09 | N/A | N/A | N/A |
| 8 | OS Independent | Jinja2 | Python | 3.1.4 | [unknown](unknown) | 2024-05-05 | N/A | N/A | N/A |
| 9 | Unknown | kiwisolver | Python | 1.4.7 | [unknown](unknown) | 2024-09-04 | N/A | N/A | N/A |
| 10 | OS Independent | MarkupSafe | Python | 2.1.5 | [https://palletsprojects.com/p/markupsafe/](https://palletsprojects.com/p/markupsafe/) | 2024-02-02 | N/A | N/A | N/A |
| 11 | Unknown | matplotlib | Python | 3.9.2 | [unknown](unknown) | 2024-08-13 | N/A | N/A | N/A |
| 12 | MacOS | numpy | Python | 2.0.2 | [https://numpy.org](https://numpy.org) | 2024-09-03 | N/A | N/A | N/A |
| 13 | Unknown | packaging | Python | 24.1 | [unknown](unknown) | 2024-06-09 | N/A | N/A | N/A |
| 14 | OS Independent | pandas | Python | 2.2.3 | [https://pandas.pydata.org](https://pandas.pydata.org) | 2024-09-20 | N/A | N/A | N/A |
| 15 | Unknown | pillow | Only | 10.4.0 | [unknown](unknown) | 2024-07-01 | N/A | N/A | N/A |
| 16 | OS Independent | pyparsing | Python | 3.1.4 | [unknown](unknown) | 2024-08-25 | N/A | N/A | N/A |
| 17 | Unknown | python-dateutil | Python | 2.9.0.post0 | [https://github.com/dateutil/dateutil](https://github.com/dateutil/dateutil) | 2024-03-01 | N/A | N/A | N/A |
| 18 | OS Independent | pytz | Python | 2024.2 | [http://pythonhosted.org/pytz](http://pythonhosted.org/pytz) | 2024-09-11 | N/A | N/A | N/A |
| 19 | OS Independent | requests | Python | 2.32.3 | [https://requests.readthedocs.io](https://requests.readthedocs.io) | 2024-05-29 | N/A | N/A | N/A |
| 20 | MacOS | scipy | Python | 1.13.1 | [https://scipy.org/](https://scipy.org/) | 2024-08-21 | N/A | N/A | N/A |
| 21 | OS Independent | seaborn | Python | 0.13.2 | [unknown](unknown) | 2024-01-25 | N/A | N/A | N/A |
| 22 | Unknown | six | 2 | 1.16.0 | [https://github.com/benjaminp/six](https://github.com/benjaminp/six) | 2021-05-05 | N/A | N/A | N/A |
| 23 | Unknown | tzdata | Python | 2024.2 | [https://github.com/python/tzdata](https://github.com/python/tzdata) | 2024-09-23 | N/A | N/A | N/A |
| 24 | OS Independent | urllib3 | Python | 2.2.3 | [unknown](unknown) | 2024-09-12 | N/A | N/A | N/A |
| 25 | Unknown | zipp | Python | 3.20.2 | [unknown](unknown) | 2024-09-13 | N/A | N/A | N/A |
| 26 | MacOS X | imageio | Python | 2.35.1 | [https://github.com/imageio/imageio](https://github.com/imageio/imageio) | 2024-08-19 | N/A | N/A | N/A |
| 27 | MacOS | pytest | Python | 8.3.3 | [unknown](unknown) | 2024-09-10 | N/A | N/A | N/A |
| 28 | Unknown | torch | Unknown | 2.4.1 | [https://pytorch.org/](https://pytorch.org/) | 2024-09-04 | N/A | N/A | N/A |
| 29 | MacOS | scikit-learn | C | 1.5.2 | [https://scikit-learn.org](https://scikit-learn.org) | 2024-09-11 | N/A | N/A | N/A |
| 30 | MacOS | keras | Python | 2.14.0 | [https://keras.io/](https://keras.io/) | 2024-08-12 | N/A | N/A | N/A |
| 31 | Unknown | tensorflow | Unknown | 2.14.0 | [https://www.tensorflow.org/](https://www.tensorflow.org/) | 2024-07-11 | N/A | N/A | N/A |
| 32 | Unknown | sklearn | Python | unknown | [unknown](unknown) | 2023-12-01 | unknown | unknown | unknown |



---
Template Copyright [openregulatory.com](https://openregulatory.com). See [template
license](https://openregulatory.com/template-license).

Please don't remove this notice even if you've modified contents of this template.