/*
  Blink

  Allume une LED pendant une seconde, puis l'éteint pendant une seconde, en boucle.
  La LED doit être connectée à la patte D2 de l'arduino
*/

/* La fonction setup() est exécutée une seule fois au démarrage.
   Le programme démarre :
    - lorqu'on alimente l'arduino
    - quand on le téléverse dans l'arduino
    - quand on appuie sur le bouton reset
 */
void setup() {
  // initialise la patte D2 en sortie
  pinMode(2, OUTPUT);
}


// La fonction loop() est exécutée en boucle tant que l'arduino est alimenté
void loop() {
  digitalWrite(2, HIGH);   // allume la LED (HIGH met D2 à 5 volt)
  delay(1000);             // attend une seconde
  digitalWrite(2, LOW);    // éteint la LED (LOW met D2 à 0 volt)
  delay(1000);             // attend une seconde
}
