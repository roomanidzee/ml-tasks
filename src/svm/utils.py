import numpy as np
import numpy.linalg as la

RADIAL_BASIS_CONSTANT = 10


def calculate_radial_basis(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.exp(
        -RADIAL_BASIS_CONSTANT * la.norm(
            np.subtract(x, y)
        )
    )
