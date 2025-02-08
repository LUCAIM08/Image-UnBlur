import cv2
import numpy as np
import argparse

def deblur_image(input_path):
    image = cv2.imread(input_path)

    if image is None:
        print(f"Errore: Immagine non trovata al percorso: {input_path}")
        return

    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    deblurred = cv2.filter2D(image, -1, kernel)

    cv2.imshow("Originale", image)
    cv2.imshow("Unblurrata", deblurred)

    print("Premi un tasto qualsiasi per chiudere le finestre...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

parser = argparse.ArgumentParser(description="Riduce il blur di un'immagine e mostra il risultato.")
parser.add_argument("input_path", type=str, help="Percorso dell'immagine blurrata.")
args = parser.parse_args()

deblur_image(args.input_path)
