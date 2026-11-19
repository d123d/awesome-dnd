# Awesome D&D [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of **open, free, and open-source Dungeons & Dragons content** — SRDs, data, APIs, code, virtual tabletops, tools, games, asset packs, AI Dungeon Masters, images, music, adventures, and reference resources.

Only content that is legally open or free is listed as *content*: the SRDs under CC-BY-4.0 / ORC / OGL, Creative Commons and public-domain material, and open-source software. Fan tools and free-tier services are marked as such. Each entry keeps its own license — check it before reuse.

**Purpose beyond the list:** this repo is also the source map for a planned **custom model trained only on D&D content** — see [MODEL.md](MODEL.md). Every entry here is a candidate corpus source, filtered by license.

## Contents

- [Official & Open Game Content](#official--open-game-content)
- [Open Data, APIs & Top GitHub Code](#open-data-apis--top-github-code)
- [Reference Sites & Resources](#reference-sites--resources)
- [Virtual Tabletops & Tables](#virtual-tabletops--tables)
- [Character Builders, Dice & Combat Trackers](#character-builders-dice--combat-trackers)
- [Generators & Map Tools](#generators--map-tools)
- [Games](#games)
- [AI Tools, Harnesses & MCP Servers](#ai-tools-harnesses--mcp-servers)
- [Asset Packs, Art, Maps, Tokens & Images](#asset-packs-art-maps-tokens--images)
- [Music & Ambience](#music--ambience)
- [Free Adventures & Supplements](#free-adventures--supplements)
- [Campaign Notes & Wikis](#campaign-notes--wikis)
- [Learning & Community](#learning--community)
- [Wikipedia](#wikipedia)
- [More Awesome Lists](#more-awesome-lists)
- [License Note](#license-note)

## Official & Open Game Content

- [D&D SRD 5.1 + SRD 5.2.1 — D&D Beyond](https://www.dndbeyond.com/srd) — Official downloads for both SRDs plus the 5.1→5.2.1 conversion guide. *CC-BY-4.0 (SRD 5.1 also under OGL 1.0a).*
- [SRD 5.2.1 PDF (direct)](https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf) — Full 2024-rules System Reference Document from Wizards of the Coast. *CC-BY-4.0.*
- [Level Up: Advanced 5E SRD (A5ESRD)](https://a5esrd.com/a5esrd) — EN Publishing's fully open, rewritten 5E SRD. *CC-BY-4.0 / OGL / ORC.*
- [Black Flag Roleplaying](https://koboldpress.com/black-flag-roleplaying/) — Kobold Press's free, open 5E-based system behind Tales of the Valiant. *ORC / CC-BY-4.0.*
- [Black Flag Reference Document (BFRD)](https://bfrd.net/) — Free online reference for Black Flag / Tales of the Valiant.
- [Free5e](https://legacy.drivethrurpg.com/browse/pub/17192/Wyrmworks?filters=44827_0_100_0_0&src=fid44827) — Community-driven open alternative to the 5e core rules, free on DriveThruRPG. *Creative Commons.*
- [13th Age SRD](https://www.drivethrurpg.com/en/product/129794/13th-Age-System-Reference-Document) — All open content from 13th Age (Heinsoo & Tweet). *OGL 1.0a.* Also on the [Internet Archive](https://archive.org/details/13thAgeSystemReferenceDocument).
- [Basic Fantasy RPG](https://www.basicfantasy.org/) — Free B/X retroclone since 2006; rules, dozens of supplements and adventures all free. *CC-BY-SA 4.0 (4e).*
- [Old-School Essentials SRD](https://ose.srd.wiki/) — OSE SRD in Markdown/wiki form; open game content under the OGL legal page [here](https://osesrd.opengamingnetwork.com/legal-information/).
- [OSRIC](https://www.mythmeregames.com/) — Retroclone of 1st-edition AD&D; OSRIC 3.0 rebuilt on CC-licensed SRD material.
- [Swords & Wizardry](https://boardgamegeek.com/rpgfamily/18544/swords-and-wizardry-and-compatible-products) — Re-creation of the original 1974 game and its supplements. *OGL 1.0a.*
- [Labyrinth Lord](https://en.wikipedia.org/wiki/Labyrinth_Lord) — Goblinoid Games B/X retroclone, free PDF, most content open. *OGL 1.0a.*
- [Cairn](https://cairnrpg.com/) — Rules-light OSR adventure game about exploring a dark Wood; quick random characters, deadly delves. Full text free. *CC-BY-SA 4.0.*
- [Worlds Without Number](https://www.drivethrurpg.com/en/product/348791/worlds-without-number) — Sine Nomine's OSR-compatible fantasy game: gritty sword-and-sorcery rules plus hundreds of pages of system-neutral worldbuilding, faction and adventure tools. *Free edition.*
- [Dungeon World SRD](https://www.dungeonworldsrd.com/) — Full text of the Powered-by-the-Apocalypse fantasy game: moves, classes, monsters, GM tools. *CC-BY 3.0.*
- [Ironsworn](https://www.ironswornrpg.com/) — Solo, co-op and guided dark-fantasy quests in the Ironlands; free to download, with oracles and asset cards. Rulebook *CC-BY-NC-SA 4.0*, SRD *CC-BY 4.0.*

## Open Data, APIs & Top GitHub Code

Star counts as of Nov 2026.

- [Azgaar/Fantasy-Map-Generator](https://github.com/Azgaar/Fantasy-Map-Generator) — ★6.2k — Interactive, highly customizable fantasy world map generator. *MIT.*
- [5e-bits/5e-database](https://github.com/5e-bits/5e-database) — ★943 — JSON database behind the D&D 5e API (archived, merged into the API monorepo). *MIT code; SRD data OGL/CC-BY.*
- [5e-bits/5e-srd-api](https://github.com/5e-bits/5e-srd-api) — ★653 — REST + GraphQL API for the 5e SRD, live at [dnd5eapi.co](https://www.dnd5eapi.co/). *MIT.*
- [foundryvtt/dnd5e](https://github.com/foundryvtt/dnd5e) — ★610 — Official Foundry VTT 5e system with SRD 5.1 + 5.2 compendium packs. *MIT; SRD content CC-BY-4.0.*
- [open5e/open5e](https://github.com/open5e/open5e) — ★460 — The Open5e reference site: SRD + open third-party 5e content.
- [open5e/open5e-api](https://github.com/open5e/open5e-api) — ★220 — Django REST API behind open5e.com; live example: `https://api.open5e.com/v1/spells/`.
- [rpgtex/DND-5e-LaTeX-Template](https://github.com/rpgtex/DND-5e-LaTeX-Template) — ★1.6k — LaTeX package to typeset beautiful 5e material.
- [game-icons/icons](https://github.com/game-icons/icons) — ★1.4k — All 4,100+ SVG icons from game-icons.net. *CC-BY 3.0.*
- [BTMorton/dnd-5e-srd](https://github.com/BTMorton/dnd-5e-srd) — ★381 — The 5e SRD converted to Markdown, JSON and YAML.
- [your5e/5e-srd-markdown](https://github.com/your5e/5e-srd-markdown) — SRD 5.1 and 5.2.1 in Markdown: single files, sections, Obsidian vault. *CC-BY-4.0.*
- [downfallx/dnd-5e-srd-markdown](https://github.com/downfallx/dnd-5e-srd-markdown) — D&D 5e (2024) SRD 5.2.1 in Markdown, complete reference.
- [knghtbrd/dnd-system-reference-document-5.1](https://github.com/knghtbrd/dnd-system-reference-document-5.1) — SRD 5.1 in Markdown, per-topic files. *CC-BY-4.0.*
- [adkinn/srd-5.2.1](https://github.com/adkinn/srd-5.2.1) — SRD 5.2.1 structured JSON dataset plus a stdio MCP server (`@adkinn/fifth-edition-srd-mcp`; monsters + conditions only — 322 monsters, 14 conditions). *CC-BY-4.0.*
- [vkama/5e-database-sqlite](https://github.com/vkama/5e-database-sqlite) — 5e-bits JSON (SRD 5.1 + 5.2) repackaged as a validated SQLite database. *MIT code.*
- [vorpalhex/srd_spells](https://github.com/vorpalhex/srd_spells) — All 5e SRD spells in one JSON list.
- [All SRD monsters in one JSON (Gist)](https://gist.github.com/tkfu/9819e4ac6d529e225e9fc58b358c3479) — Single-file SRD monster data.
- [dnd-5e-core (PyPI)](https://pypi.org/project/dnd-5e-core/) — Offline Python rules engine with bundled SRD JSON: monsters, spells, classes, items, combat.
- [dnd5epy (PyPI)](https://pypi.org/project/dnd5epy/) — Python client/docs for the dnd5eapi.co REST + GraphQL API. *MIT.*
- [5e-bits/awesome-5e-srd](https://github.com/5e-bits/awesome-5e-srd) — Projects, clients, bots and apps built on the 5e SRD API.

## Reference Sites & Resources

- [donjon](https://donjon.bin.sh/) — The DM's utility belt: dungeon/inn/NPC generators, encounter and treasure tools, fantasy calendars, name generators. *Free.*

- [5etools](https://5e.tools/) — Browser suite for 5e players and DMs: bestiary, spells, classes, loot generator, DM screen. *Fan reference tool, not official WotC; free.*
- [Open5e](https://open5e.com/) — Open-source SRD reference site and API for 5e monsters, spells, classes and open third-party content.
- [The Hypertext d20 SRD](https://www.d20srd.org/) — Indexed, hyperlinked SRDs for 3.5, 5e and Pathfinder. *OGL / open content.*
- [D&D Beyond — Basic Rules](https://www.dndbeyond.com/sources/dnd/basic-rules-2014) — Official free Basic Rules + SRD content with a free-tier character builder.
- [Roll20 5e SRD Compendium](https://app.roll20.net/forum/post/2877778/update-1-slash-26-5th-edition-srd-mega-update-new-sheet-new-compendium-plus-compendium-drag-and-drop-integration/) — Free SRD compendium and OGL character sheet at the free subscription level.
- [D&D 5e API](https://www.dnd5eapi.co/) — Free, no-auth REST API for SRD-only 5e data.

## Virtual Tabletops & Tables

- [RPTools/MapTool](https://github.com/RPTools/maptool) — Mature, system-agnostic VTT for remote or face-to-face play. *AGPL-3.0.*
- [Kruptein/PlanarAlly](https://github.com/Kruptein/PlanarAlly) — Self-hosted browser VTT: dynamic lighting, vision, layers, initiative. *MIT.*
- [dungeon-revealer/dungeon-revealer](https://github.com/dungeon-revealer/dungeon-revealer) — Self-hosted app to reveal map areas, move tokens, roll dice, share notes.
- [drwhut/tabletop-club](https://github.com/drwhut/tabletop-club) — Physics-based 3D tabletop simulator in Godot. *MIT.*
- [AleVersace/Vers](https://github.com/AleVersace/Vers) — Open-source VTT with grid-snapped tokens, measurements, reusable dice buttons. *AGPL-3.0.*
- Foundry VTT dnd5e system — official 5e system for Foundry; listed once under [Open Data, APIs & Top GitHub Code](#open-data-apis--top-github-code).
- [Owlbear Rodeo Dice](https://github.com/owlbear-rodeo/dice) — Official 3D dice extension for Owlbear Rodeo. *GPL-3.0.*
- [DominoPivot/obr-extensions](https://github.com/DominoPivot/obr-extensions) — Owlbear Rodeo extension collection via GitHub Pages.
- [autorolltables](https://autorolltables.github.io/) — Auto-rolling random tables for tabletop RPGs. Repo: [autorolltables/autorolltables.github.io](https://github.com/autorolltables/autorolltables.github.io).
- [BigJk/snd](https://github.com/BigJk/snd) — Sales & Dungeons: thermal-printer utility for D&D/TTRPG handouts and tables.

## Character Builders, Dice & Combat Trackers

- [avrae/avrae](https://github.com/avrae/avrae) — Discord bot for D&D 5e: dice, sheet import, initiative tracking. *GPL-3.0.*
- [Aurora Builder elements](https://github.com/aurorabuilder/elements) — Content files for Aurora, the 5e character builder with SRD content and PDF export.
- [Arcanum / d20.build](https://github.com/MashhuMaximilian/Arcanum) — Web-based 5e character creation tool inspired by Aurora (Next.js).
- [dice-roller](https://github.com/dice-roller) — Advanced JS dice-roller org: core library, CLI, Vue components. *MIT.*
- [xdaybreakerx/js-d20](https://github.com/xdaybreakerx/js-d20) — NPM dice roller for any tabletop RPG, Avrae-style syntax. *MIT.*
- [cynicaloptimist/improved-initiative](https://github.com/cynicaloptimist/improved-initiative) — Combat tracker for D&D 5e. *MIT.*
- [Paul-Ladyman/dnd-battle-tracker](https://github.com/Paul-Ladyman/dnd-battle-tracker) — Offline web initiative and combat tracker for 5e. *MIT.*
- [santiagoclv/dnd-combat-tracker](https://github.com/santiagoclv/dnd-combat-tracker) — Tablet-friendly combat tracker: initiative and HP, no keyboard needed.
- [adventurerscodex/adventurerscodex](https://github.com/adventurerscodex/adventurerscodex) — Character sheet and campaign tool: "the next step in tabletop RPGs."
- [Kobold Plus Fight Club](https://koboldplus.club/) — Encounter builder for 5e with XP budgeting and SRD + imported monster sources. *Free.*

## Generators & Map Tools

- [Azgaar's Fantasy Map Generator](https://azgaar.github.io/Fantasy-Map-Generator/) — Free web app for interactive, customizable SVG world maps.
- [Dungeon Scrawl](https://app.dungeonscrawl.com/) — Free browser dungeon-map drawing with VTT/print export and procedural dungeons in beta.
- [Watabou's Procgen Arcana](https://watabou.itch.io/medieval-fantasy-city-generator) — Procedural cities, villages, one-page dungeons, caves and regions; PNG/SVG/JSON export.
- [Eigengrau's Essential Establishment Generator](https://github.com/ryceg/Eigengrau-s-Essential-Establishment-Generator) — ★894 — Town generator ready for out-of-the-box play in any fantasy TTRPG.
- [OpenDnD Personae](https://www.skypack.dev/view/@opendnd/personae) — CLI that generates NPCs/characters with abilities and family. *MIT.*
- [LeoColman/rpg-npc-generator](https://github.com/LeoColman/RPG-NPC-Generator) — NPC generator app: name, profession, personality, AI portrait, optional 5e stat block.
- [deadmate/foundry-vtt-simple-npc-generator](https://github.com/deadmate/foundry-vtt-simple-npc-generator) — Foundry dnd5e toolkit: NPC, encounter and shop generation.
- [ebshimizu/5e-monster-maker](https://github.com/ebshimizu/5e-monster-maker) — Monster stat block builder for 5e.
- [Mike-Risher/5e-DnD-Character-Generator](https://github.com/Mike-Risher/5e-DnD-Character-Generator) — JavaScript 5e character generator.
- [mak-kirkland/chronicler](https://github.com/mak-kirkland/chronicler) — ★743 — Free, offline worldbuilding tool and local wiki for writers and GMs.

## Games

- [NetHack](https://github.com/NetHack/NetHack) — The classic roguelike: descend the Mazes of Menace for the Amulet of Yendor. *NetHack GPL.*
- [Dungeon Crawl Stone Soup](https://github.com/crawl/crawl) — Single-player roguelike of dungeon exploration, combat and magic. *GPL-2.0+.*
- [Shattered Pixel Dungeon](https://github.com/00-evan/shattered-pixel-dungeon) — Open-source roguelike with randomized levels and hundreds of items. *GPL-3.0.*
- [Pixel Dungeon](https://github.com/watabou/pixel-dungeon) — Watabou's traditional roguelike, basis of Shattered Pixel Dungeon. *GPL-3.0.*
- [Angband](https://github.com/angband/angband) — Tolkien-universe dungeon roguelike: 100 levels to Morgoth. *GPL-2.0.*
- [Cataclysm: Dark Days Ahead](https://github.com/CleverRaven/Cataclysm-DDA) — Turn-based survival roguelike, procedurally generated world. *CC-BY-SA 3.0.*
- [ArchaicQuest](https://github.com/LiamKenneth/ArchaicQuest) — Browser-playable MUD (text MMORPG) in C#.
- [Project Infinity](https://github.com/electronistu/Project_Infinity) — Browser-based 5e-compatible RPG with an AI Dungeon Master that rolls real dice.
- [DungeonMind](https://charles-forsyth.github.io/dungeonmind-rs/) — Self-learning Q-learning roguelike: 8 procedural floors, 13 D&D monster archetypes, d20 rolls.
- [pitchblack-rpg](https://github.com/kartikcho/pitchblack-rpg) — Interactive text adventure with D&D-style gameplay in Python.

## AI Tools, Harnesses & MCP Servers

- [Skeinkeeper](https://github.com/skeinkeeper/skeinkeeper) — Self-hosted AI Dungeon Master: joins Discord voice, speaks in character voices, drives Foundry VTT, persistent campaign state. *Apache-2.0.*
- [samvoisin/ai-dungeon-master](https://github.com/samvoisin/ai-dungeon-master) — AI game master your party talks to through Discord (GPT-4 + LlamaIndex, 5e rules).
- [omervaner/ai-dungeon-master](https://github.com/omervaner/ai-dungeon-master) — Text fantasy RPG with AI DM; Groq cloud or local Ollama. *MIT.*
- [neuralinitiative/claude-dnd-skill](https://github.com/neuralinitiative/claude-dnd-skill) — Unofficial D&D 5e DM skill for Claude Code: persistent campaigns, full 5e mechanics.
- [Claude-Code-Game-Master](https://github.com/Sstobo/Claude-Code-Game-Master) — Agent harness: drop in a book/PDF, RAG extracts characters/locations/items, play in that world with specialist agents + D&D 5e API.
- [claude-dnd (peonic)](https://www.peonic.net/projects/claude-dnd/) — Template for running full 5e campaigns with Claude Code as DM in the terminal; SRD included, persistent worlds via Git branches.
- [1A7432/loreweaver](https://github.com/1A7432/loreweaver) — Self-hosted, world- and story-first AI Game Master for TTRPGs (D&D 5e).
- [diceframe/diceframe](https://github.com/diceframe/diceframe) — Self-hostable AI tabletop RPG platform, multiple rule systems (D&D, CoC, freeform).
- [Frichetten/Dungeons-and-Agents](https://github.com/Frichetten/Dungeons-and-Agents) — Reference pattern for agent campaign state: per-campaign SQLite + append-only event log + snapshot/transcript, every mutation forced through a `dmctl` CLI (agenda/campaign/clock/combat/dice/faction/item/npc/quest/recap/secret/state/validate/…). *No license file — pattern reference only.*
- [procload/dnd-mcp](https://github.com/procload/dnd-mcp) — MCP server implementation of the D&D 5e API: resources, tools, prompts.
- [frap129/lorekeeper-mcp](https://github.com/frap129/lorekeeper-mcp) — MCP server for semantic search/lookup of 5e data via the Open5e API.
- [KoboldAI Client](https://github.com/KoboldAI/KoboldAI-Client) — Browser front-end for AI writing and AI Dungeon-style Adventure mode, local or remote models. *AGPL.*
- [KoboldCpp](https://github.com/LostRuins/koboldcpp) — GGUF model runner for local LLM storytelling and AI Dungeon-style play.
- [SillyTavern](https://github.com/SillyTavern/SillyTavern) — LLM front-end/harness for AI roleplay: character cards, lorebooks, group chats; connects to KoboldCpp, Ollama, OpenAI, Claude, OpenRouter. *AGPL-3.0.*

## Asset Packs, Art, Maps, Tokens & Images

- [ASSETS.md](ASSETS.md) — The full asset index: maps, tokens, art, stats & data, handouts, VTT libraries, audio and generators, each with access and license notes.
- [Game-icons.net](https://game-icons.net/) — 4,100+ free SVG icons: weapons, spells, creatures, items. *CC-BY 3.0, some CC0.*
- [OpenGameArt.org](https://opengameart.org/) — Huge community library of 2D/3D art, tiles, sprites, music and SFX. *Per-asset CC0 / CC-BY / CC-BY-SA / GPL — check each.* [Fantasy search](https://opengameart.org/art-search-advanced?field_art_tags_tid=Fantasy&field_art_type_tid%5B0%5D=9&sort_by=count&sort_order=DESC&page=8).
- [Kenney](https://kenney.nl/assets) — Thousands of sprites, tilesets, 3D models, UI and audio packs. *CC0, no credit required.*
- [Forgotten Adventures](https://www.forgotten-adventures.net/) — Top-down tokens, battlemaps and mapmaking assets for Foundry/Roll20/Dungeondraft; free Core Mapmaking Pack, originals free for personal use.
- [FA Free Creature Tokens Pack 2](https://cartographyassets.com/assets/4958/creature-tokens-pack-2/) — 40+ free 400dpi PNG creature tokens (CR 0, G–W).
- [2-Minute Tabletop](https://2minutetabletop.com/) — Hand-drawn battlemaps and 8,000+ tokens; token library free, base map packs pay-what-you-want.
- [8x8 Fantasy RPG Pixel Sprites (itch.io)](https://pulsarcp.itch.io/8x8-rpg-sprite) — 2,782 free 8x8 sprites: monsters, characters, items, tiles.
- [Ashen Wilds Starter (itch.io)](https://ritzman99.itch.io/ashen-wilds-gathering-crafting-starter) — 20 free fantasy props with 38 states: nodes, stations, crops, fishing gear.
- [itch.io game assets — free, top rated](https://itch.io/game-assets/free) — The firehose: thousands of free tilesets, sprites, tokens and UI packs.
- [RPG-Awesome](https://nagoshiashumari.github.io/Rpg-Awesome/) — 495 fantasy font/CSS icons derived from Game-icons.net, for web sheets and handouts.
- [Bryans FoundryVTT Assets list](https://github.com/bryancasler/Bryans-FoundryVTT-Assets-And-Resources) — GitHub list of free Foundry map packs and token resources.
- [Wikimedia Commons — St. George and the Dragon (Novgorod icon)](https://commons.wikimedia.org/wiki/File:George_novgorod.jpg) — 15th-century dragon-slaying icon, handout-ready. *Public domain.*
- [Wikimedia Commons — Rackham, Fafner the Dragon](https://commons.wikimedia.org/wiki/File:Ring30.jpg) — Arthur Rackham's 1910 Fafner illustration. *Public domain.*

## Music & Ambience

- [Tabletop Audio](https://tabletopaudio.com/) — Original 10-minute ambiences and music for fantasy, sci-fi, horror and nature scenes. *Free to stream/use at the table.*
- [Michael Ghelfi Studios](https://michaelghelfistudios.com/) — Film-quality RPG ambience and music; large free portion on YouTube/Bandcamp.
- [Incompetech — Kevin MacLeod](https://incompetech.com/) — 2,000+ royalty-free tracks. *CC-BY 4.0 with credit.*
- [Syrinscape Radio](https://syrinscape.com/radio/) — Free streaming RPG ambient sound and music channels.
- [DnD Soundboard](https://dndsoundboard.com/) — 100+ looping music, ambience and SFX scenes in the browser. *Free tier.*
- [SFXMint D&D Soundboard](https://sfxmint.com/soundboard/dnd) — 16 free D&D sound buttons and loops, MP3 download. *CC0.*

## Free Adventures & Supplements

- [DMs Guild — Pay What You Want](https://www.dmsguild.com/en/browse?pwyw=true) — Community marketplace filtered to PWYW: *A Most Potent Brew*, *First Blush*, *An Ogre and His Cake* — set price to $0.
- [DriveThruRPG — WotC free titles](https://www.drivethrurpg.com/en/publisher/44/Wizards-of-the-Coast) — WotC catalog including free items like *The Barber of Silverymoon*.
- [Free D&D One-Shots — Anvil & Ink](https://anvilnink.com/free-dnd-one-shots/) — Vetted genuinely-free one-shots, incl. Colville's *The Delian Tomb* and *A Wild Sheep Chase* (PWYW).
- [Free Official D&D Resources — Nerdist](https://nerdist.com/article/free-dungeons-dragons-official-resources-adventures/) — Roundup of official free WotC material: *Defiance in Phlan*, *Adventure with Muk*, more.
- [Rand Roll — Free Fantasy PDFs](https://www.randroll.com/guide-free-pdfs-fantasy/) — Guided list of free/PWYW fantasy, solo, city, dungeon and random-table PDFs on DriveThruRPG.
- [Basic Fantasy adventures](https://www.basicfantasy.org/downloads.html) — Dozens of complete adventures and supplements, free PDFs, print at cost. *Open license.*

## Campaign Notes & Wikis

- [The Homebrewery](https://homebrewery.naturalcrit.com/) — Write homebrew in Markdown, get documents that look like official 5e books. *Free.*
- [GMBinder](https://www.gmbinder.com/) — Homebrew document builder in the official 5e style, with sharing and print/PDF export. *Free tier.*
- [Kanka](https://kanka.io/) — Collaborative worldbuilding and campaign manager: characters, locations, timelines, maps and journals. Source at [owlchester/kanka](https://github.com/owlchester/kanka). *Free tier; source-available, self-hostable.*

- [Obsidian TTRPG Community](https://github.com/Obsidian-TTRPG-Community) — Dice roller, statblocks and more D&D plugins for Obsidian.
- [Obsidian Dice Roller](https://github.com/Obsidian-TTRPG-Community/dice-roller) — Inline dice rolling in notes: `dice: 2d6+3` (formerly javalent/dice-roller).
- [fantasy-statblocks](https://github.com/Obsidian-TTRPG-Community/fantasy-statblocks) — ★502 — D&D-style statblocks inside Obsidian.
- [dnd5e-markdown (Obsidian)](https://github.com/Obsidian-TTRPG-Community/dnd5e-markdown) — The 5e SRD in Markdown for Obsidian, plus homebrew space.
- [Atlas VTT for Obsidian](https://atlas-vtt.dev/) — VTT inside Obsidian: maps, tokens, fog of war, dice, initiative; 5e presets. *AGPL.*
- rpgtex LaTeX template — typeset homebrew books that look like official 5e; listed once under [Open Data, APIs & Top GitHub Code](#open-data-apis--top-github-code).

## Learning & Community

- [Sly Flourish](https://slyflourish.com/) — Lazy DM advice and the free Lazy GM's Resource Document.
- [The Alexandrian](https://thealexandrian.net/about) — Justin Alexander's GM archive: Three Clue Rule, node-based design, Gamemastery 101.
- [Matt Colville — Running the Game](https://www.youtube.com/@MattColville) — The free YouTube series that taught a generation to DM; home of *The Delian Tomb*.
- [Miserlou/dnd-tldr](https://github.com/Miserlou/dnd-tldr) — ★687 — Dungeons & Dragons, too long; didn't read: the rules, condensed.
- [Free RPGs — John H. Kim](https://www.darkshire.net/jhkim/rpg/freerpgs/fulllist.html) — 500+ free RPGs with author, description and format.
- [Solo RPG Resources](https://robmaule.github.io/Solo-RPG-Resources-Revised/) — Solo systems, oracles and tools, incl. free Ironsworn.
- [TTRPG Websites — Orey](https://orey.github.io/blog/links-en/) — Index of RPG forums, wikis, SRDs and publisher sites by system.

## Wikipedia

All *CC-BY-SA*.

- [Dungeons & Dragons](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons) — History, play and publication since 1974.
- [Portal: Dungeons & Dragons](https://en.wikipedia.org/wiki/Portal:Dungeons_%26_Dragons) — Index of all D&D articles.
- [System Reference Document](https://en.wikipedia.org/wiki/System_Reference_Document) — What an SRD is; WotC SRDs from 3e to 5.2.
- [Open Game License](https://en.wikipedia.org/wiki/Open_Gaming_License) — OGL history, the 2023 controversy, SRD 5.1's move to CC-BY-4.0.
- [Open gaming](https://en.wikipedia.org/wiki/Open_gaming) — The open gaming movement and free-culture licensed games.
- [d20 System](https://en.wikipedia.org/wiki/D20_System) — The d20 System, its SRD, and Open Game Content.
- [D&D campaign settings](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons_campaign_settings) — Greyhawk, Dragonlance, Forgotten Realms, Eberron, Ravenloft, Dark Sun, Planescape…
- [Forgotten Realms](https://en.wikipedia.org/wiki/Forgotten_Realms) — Ed Greenwood's Faerûn.
- [Dragonlance](https://en.wikipedia.org/wiki/Dragonlance) — Weis & Hickman's Krynn.
- [Eberron](https://en.wikipedia.org/wiki/Eberron_Campaign_Setting) — Keith Baker's pulp-noir magitech setting.
- [Greyhawk / Flanaess](https://en.wikipedia.org/wiki/Flanaess) — Gygax's World of Greyhawk.
- [D&D retro-clones](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons_retro-clones) — OSRIC, Labyrinth Lord, Swords & Wizardry, Basic Fantasy, the OSR.

## More Awesome Lists

- [flamableconcrete/awesome-dnd](https://github.com/flamableconcrete/awesome-dnd) — ★307 — The original curated D&D resources list.
- [HenriqueLebre/awesome-ttrpg-tools](https://github.com/HenriqueLebre/awesome-ttrpg-tools) — Awesome TTRPG tools (successor to the removed TheMrEvil list).
- [Zireael07/awesome-tabletop-rpgs](https://github.com/Zireael07/awesome-tabletop-rpgs) — Free and open-source tabletop RPGs.
- [Billiam/awesome-ironsworn](https://github.com/Billiam/awesome-ironsworn) — Ironsworn projects, tools and resources.
- [Useful D&D links (Gist)](https://gist.github.com/markhamersma/94749e5d1398e6c34f5fb8e746d21cf6) — Community link list for play and prep.
- [FMHY — Tabletop Tools](https://fmhy.net/) — Free-media index with a tabletop tools section.

## License Note

This list is a directory of links. The list itself is released under CC0. Linked content keeps its own license: SRD material is CC-BY-4.0 (Wizards of the Coast), other systems are ORC / OGL / CC as marked, software is under its repo license, and fan tools like 5etools are free to use but not open content. **No copyrighted D&D book text belongs here** — open content only.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: one entry per PR, link must be live, content must be open-licensed or genuinely free, and say the license if you know it. Especially wanted: entries that are also clean **training-corpus sources** for [MODEL.md](MODEL.md).
