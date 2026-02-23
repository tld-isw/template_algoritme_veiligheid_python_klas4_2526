# BASIS SOLO

## Programmeren
Je bewerkt alleen `ransomware.py`. Hierin zet je je naam en bewerk je de code. Dit is ook het enige bestand wat je hoeft in te leveren.

## Programma draaien
Klik vanuit `app.py` op play.

Het programma leest `cases.json`, dit zijn de organisaties/casussen die je hebt geanalyseerd in de opdracht met een extra.
Het programma berekent per casus een score en geeft een label:
LAAG / MIDDEL / HOOG

## Velden in `cases.json` (features)

Je gebruikt in `calculate_risk(features)` alleen objectieve checks op basis van `features`.

### Kernvelden (deze zijn relevant voor de opdracht en worden gebruikt in de zichtbare tests)
| Veld | Betekenis | Mogelijke waarden | Tip |
|---|---|---|---|
| `auto_updates` | Automatische updates/patching | `true` / `false` | `false` = vaker kwetsbaarheden |
| `mfa` | Multifactorauthenticatie | `true` / `false` | `false` = accounts sneller misbruikt |
| `offline_backups` | Offline back-ups aanwezig | `true` / `false` | `false` = impact groter |
| `backups_tested` | Back-ups getest (restore test) | `true` / `false` | `false` = schijnveiligheid |
| `incident_plan` | Incidentresponsplan aanwezig | `true` / `false` | `false` = trager/chaotischer herstel |
| `security_training` | Securitytraining frequentie | `false` of `"yearly"` of `"twice_yearly"` | `"twice_yearly"` is beter dan `"yearly"`, `false` is slechtst |
| `network_segmentation` | Netwerksegmentatie | `true` / `false` | `false` = verspreiding makkelijker |
| `unsupported_os` | Verouderd/niet-ondersteund OS aanwezig | `true` / `false` | `true` = extra kwetsbaar (omgekeerde logica) |


## Tests draaien (visible)
Ga naar de terminal (CTRL `; dit zit boven de tab)
Typ in de terminal het commando:
pytest basis_solo

Als de tests groen zijn, voldoet je algoritme aan de zichtbare eisen.
Er zijn ook onzichtbare testen die de docent gebruikt voor het testen.
