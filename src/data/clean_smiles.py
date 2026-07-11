###Imports
from rdkit import Chem 
###Main Function 
def canonicalize(smiles: str) -> str | None:
# convert SMILES string into an RDKit molecule
    molecule = Chem.MolFromSmiles(smiles)


# What value does RDKit return when parsing fails?
    if molecule is None:
        return None
    return Chem.MolToSmiles(molecule)
