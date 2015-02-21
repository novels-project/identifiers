# Novels Project Identifiers

The file `novels-project-identifiers.json` contains a mapping between
bibliographic identifiers. The keys in the JSON dictionary are Novels Project
identifiers (integers starting with 1) and the values are other canonical identifiers
of bibliographic identifiers.

For example, the novel with Novels Project identifier 68 is Charlotte Smith's
*Letters of a Solitary Wanderer* (1800). This novel also appears in Garside,
Raven, and Schöwerling's *Bibliographical Survey of Prose Fiction Published in
the British Isles* with an identifier `1800A068`. So part of the `novels-project-identifiers.json`
file looks like this:

```json
"68": {
  "novels-project": 68,
  "garside-raven-schöwerling": "1800A068"
}
```

The data format used is UTF-8 encoded JSON. Corrections are welcome.
