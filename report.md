# Bronze Age Game Logic Analysis
## Architecture & Code Structure
The game is built using Unity and compiled via IL2CPP to WebAssembly (WebGL). The primary game logic is contained within `Assembly-CSharp.dll`.

### Key Classes
- **Village**: The main game controller that manages the turns (e.g. `yearUpdate()`, `OnEndTurn()`), the map regions (africaGameField, nearEastGameField), and UI events (buttons for tech, buildings, evolution).
- **SaveObject**: This acts as the main game state. It stores crucial variables like `turnNum`, `yearNum`, `peopleNum`, `foodTotalGrowNum`, `prodGrowNum`, `cultGrowNum`, `powerNum`, and `evolutionPointsNum`. It also tracks worker placement (e.g. `workersAtWoodNum`, `workersAtSavannaNum`).
- **Tech & Technologies**: Represents the tech tree. A `Tech` has properties like `level`, `reqTech1`, `reqTech2`, and costs. `Technologies` handles unlocking them.
- **Build & Buildings**: Represents constructed structures in the village. Similar to Tech, it manages the `level`, `isAvail()`, and unlocks (`levelUp()`).
- **Human**: Represents units/workers that are assigned to different `GamePanel` regions to gather resources.
- **GameEvent**: Handles random or scripted events that occur each turn, which may impact `correntRisk` or give bonuses.

## Core Gameplay Loop
The gameplay loop is turn-based. Each turn (handled by `Village.OnEndTurn()`), the game calculates resource generation based on the workers assigned to different regions (Wood, Savanna, River, Plant, Mount, Desert). The calculations rely on modifiers (`foodModNum`, `prodModNum`, `cultModNum`, `powerModNum`) which are upgraded by buildings and technologies.

### Resources
1. **Food**: Drives population growth (`peopleGrowNum`).
2. **Production (Prod)**: Used to construct `Build` entities.
3. **Culture (Cult)**: Generates Tech/Evolution points.
4. **Power**: Calculated for risk management (`correntRisk`).

### Eras and Turns
The game is divided into Eras defined in the `Const` class:
- ERA_1_TURN to ERA_6_TURN
- END_BC1_TURN, END_BC2_TURN
The `turnNum` variable tracks progress across these eras.

## Localization and Strings
We successfully extracted the `TextAsset` files from `data.unity3d`. The game supports multiple languages (English, Russian, Spanish, French, etc.) via localization files like `strings_en_US.txt`. These files define all UI strings, including button text (`"settlementButtonString"`, `"techButtonString"`), credits, tooltips, and dialogues, confirming a standard key-value map for localizations.

## Reverse Engineering Method
1. The `.wasm` file (`WebGL.wasm`) along with `global-metadata.dat` (from `WebGL.data`) were analyzed using `Il2CppDumper`.
2. This yielded `DummyDlls`, specifically `Assembly-CSharp.dll`, which contained the game logic structure (classes, fields, methods).
3. We used `monodis` to decompile the structure of these Dummy DLLs.
4. The `data.unity3d` archive was extracted using `UnityPy` to obtain configuration and text files.
