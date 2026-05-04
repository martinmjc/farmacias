## Mathematical Model Implementation
This code implements a mathematical optimization model for planning the purchase and inventory of medicines required to treat different diseases over multiple periods.

The model considers three main sets:

- `I`: set of medicines.
- `J`: set of diseases.
- `T`: set of planning periods.

The objective is to minimize the total purchasing cost of medicines. Two types of purchases are considered:

- Purchases using the AGEMED reference price (`PRA`).
- Extra purchases using the external reference price (`PRE`).

The model first estimates the medicine requirements for each disease based on the number of cases and the required dosage. Then, it adjusts the projected demand using historical consumption data from previous periods. This allows the model to estimate future demand for each medicine.

The implementation also includes inventory logic. The available stock of each medicine is converted into months of existence (`MED`) and compared with an upper limit (`LS`). If the stock level is below the established limit, the model activates a purchase decision through the binary parameter `P`.

A safety inventory level (`H`) is also calculated as a percentage of the projected demand. This prevents excessive stock accumulation while ensuring that a minimum reserve is maintained.

The decision variables of the model are:

- `w[i,j,t]`: planned quantity of medicine `i` assigned to disease `j` in period `t`.
- `x[i,j,t]`: extra quantity of medicine `i` assigned to disease `j` in period `t`.
- `S[i,t]`: inventory level of medicine `i` at the end of period `t`.

The model is subject to the following main constraints:

1. Demand and inventory balance:  
   The previous inventory plus planned and extra purchases must cover the projected demand and the final inventory.

2. Safety inventory limit:
   The final inventory of each medicine must not exceed the safety inventory level.

3. Budget constraint:
   Purchases using the AGEMED reference price must not exceed the available budget ceiling (`TP`).

4. Purchase activation constraint: 
   Purchases are only allowed when the medicine stock level is below the established months-of-existence limit.

In summary, the code solves a medicine procurement planning problem by deciding how much to purchase through regular and extra sources, while considering projected demand, available inventory, safety stock, and budget limitations.

## Estructura
- `main.py`: punto de entrada
- `src/funciones.py`: funciones principales
- `tests/`: pruebas
- `data/input` : datasets usados como entrada al modelo
- `data/output` : guardar resultados del model

## Ejecución
```bash
python main.py