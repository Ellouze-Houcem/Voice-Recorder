import sounddevice
from scipy.io.wavfile import write

def voice_recorder(seconds, file):
    """
    Enregistre la voix pendant un certain nombre de secondes et sauvegarde le résultat dans un fichier WAV.

    Paramètres :
    - seconds (int) : Le nombre de secondes pour l'enregistrement.
    - file (str) : Le nom du fichier WAV dans lequel enregistrer le son.

    Retour :
    Aucun.

    Remarque :
    Assurez-vous d'installer les bibliothèques nécessaires en utilisant :
    pip install sounddevice scipy
    """

    # Affiche un message indiquant le début de l'enregistrement.
    print("Recording Started…")

    # Enregistre le son pendant le nombre de secondes spécifié.
    recording = sounddevice.rec((seconds * 44100), samplerate=44100, channels=2)
    
    # Attendez que l'enregistrement soit terminé.
    sounddevice.wait()
    
    # Écrit le fichier WAV avec le son enregistré.
    write(file, 44100, recording)
    
    # Affiche un message indiquant la fin de l'enregistrement.
    print("Recording Finished")

# Appelle la fonction voice_recorder avec une durée de 10 secondes et un nom de fichier "record.wav".
voice_recorder(10, "record.wav")
