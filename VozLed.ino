bool titilando = false;  // Estado del LED titilando

void setup() {
  Serial.begin(9600);       // Inicia comunicación serial
  pinMode(13, OUTPUT);      // Configura el pin 13 como salida
}

void loop() {
  // Verifica si hay datos nuevos por el puerto serial
  if (Serial.available()) {
    String comando = Serial.readStringUntil('\n');  // Lee hasta salto de línea
    comando.trim();  // Elimina espacios en blanco

    if (comando == "enciende") {
      digitalWrite(13, HIGH);   // Enciende LED
      titilando = false;        // Detiene titilado si estaba activo
    } else if (comando == "apaga") {
      digitalWrite(13, LOW);    // Apaga LED
      titilando = false;
    } else if (comando == "titila") {
      titilando = true;         // Activa modo titilar
    }
  }

  // Si está en modo titilar, parpadea el LED
  if (titilando) {
    digitalWrite(13, HIGH);
    delay(300);
    digitalWrite(13, LOW);
    delay(300);
  }
}