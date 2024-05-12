var lightSubtitles = [
            "La realidad no es como en las canciones. La Batalla del Vado Rojo no tuvo nada de gloriosa. ¿O acaso hay gloria en los estandartes quemados? ¿Donde se encuentra la belleza en un cementerio de caballos cercenados? ¿Tiene algo de honorable cruzar un río sobre cadáveres amontonados, con las botas llenándose no de agua, sino de sangre? No había nada de lo que estar orgullosos. Y lo celebramos igualmente. Celebramos todas esas heroicidades macabras. Porque a pesar de todo, nosotros seguíamos vivos.",
            "Lo bello del desierto es que en algún lugar de su vastedad esconde un oasis.",
            "La voz convivía en mi mente, me gritaba por las mañanas, me susurraba por las noches. El Otro nunca dormía. El Otro siempre estaba ahí.",
            "El interés nacional requiere que se traicione, que se mienta y que se masacre.",
            "El único mapa que vale en el desierto está en el cielo.",
            "No se sabe cómo ni cuándo la nuez de areca y la hoja de betel, productos estimulantes totalmente distintos, fueron utilizados por primera vez juntos. Se han hallado indicios que prueban que ambas sustancias se mascan juntas desde hace al menos cuatro siglos en las aldeas paloas. En la cultura paloa se le daba un gran simbolismo al hecho de que se unan la nuez y la hoja, utilizándose en rituales del matrimonio.",
            "Con la victoria en los Montes del Alpe y la anexión de Vil’Passe, Mohad acabó con las ambiciones expansionistas del Emperador suná Moshi XI. Tras la muerte de este emperador y la coronación de su hijo empezó un periodo de relativo entendimiento entre ambas potencias.",
            "Comercia con tu enemigo hasta que la mera posibilidad de empezar una guerra deje de tener sentido.",
            "Si el desierto no te mata, te endurece. Si el desierto no te endurece, te vuelve loco.",
            "Gobernar no consiste en solucionar problemas, sino en hacer callar a los que los provocan. De un modo u otro.",
            "Es el sol, tranquilo y silencioso, el mayor asesino del desierto.",
            "El hombre sano no tortura a otros, por lo general es el torturado el que se convierte en torturador.",
            "El rey que es amado por su pueblo puede ser bueno, pero el rey que ama a su pueblo es mejor.",
            "Existen dos tipos de surcados: los que despertaron a un demonio ajeno y los que conviven con el suyo propio. Los primeros son imprevisibles, incontrolables. Con los segundos, en cambio, se puede trabajar.",
        ];

        var darkSubtitles = [
            "Tras calcinar por completo la ciudad sagrada de la Jungla Perdida, el Jinete Loco decidió darse muerte por sí mismo. Su cuerpo fue encontrado en el fondo del Mar Cerrado, con un lastre atado al tobillo y Kaaldanor entre sus costillas.",
            "No podíamos hacer prisioneros. Incluso teníamos órdenes de no divertirnos con sus mujeres. Pasamos por el hacha y la espada todo lo que respiraba. Pero no fuimos lo bastante rápidos. Los jinetes llegaron raudos y sus monturas nos escupieron la muerte a la cara. Lo abrasaron todo: las casas, los muertos, los vivos, las armas. Fui lo único que dejaron con vida y me dejaron ir con una mano menos y el cuerpo lleno de ampollas en carne viva. Solo para que os lo contara, señor.",
            "Es el Khaz Dolu quien elige a sus cuatro Maestros, y son los cuatro Maestros quienes eligen al Khaz Dolu.",
            "Kud Si Fana, así lo llamaban los habitantes de las cumbres más bajas, que eran como gigantes de roca helada. Eran sus Apos, capaces de rugir y escupir sus entrañas para enterrar aldeas enteras en el hielo. No, para ellos no son montañas, son mucho más, son sus dioses.",
            "¿Que si fue duro? Oh, bueno… Nos despertaban a la hora del lobo para salir a correr por la nieve a una altitud a la que no vuelan ni las águilas. Nos hacían mantener pesadas rocas en alto hasta desfallecer en mitad de la ventisca. Nos hacían luchar unos con otros, con los puños, con barras de hierro, y con una sola prenda, una venda para los ojos. Nos abandonaban en mitad de los glaciares, a varias leguas de la base, y se largaban en dragón abandonándonos a nuestra suerte.",
            "Al final de los cinco años en la Burbúja, un magno ha de ser capaz de saltar por encima de alguien de su misma estatura, pasar bajo una vara a la altura de su rodilla, quitarse una piedra de la bota mientras corre en los bosques sin romper ni una sola rama u hoja, defenderse ante nueve espadas corrientes y, sobre todo, recitar quince libros de poesía.",
            "Anda saltando mi sapito,\nde charquito en charquito.\nCome moscas y mosquitos,\nY a ninguno le hace asquitos.",
            "Un jinete de dragón ha de tener fría la cabeza, pero calor en el corazón.",
            "Kaaldanor nació del deseo del Khaz Dolu de mostrar a todo el mundo las maravillas que se hacían en la Forja de Dar Shi Ben. El encargo supuso la primera espada forjada con garra de dragón. Tras abandonar el gremio, el Jinete Loco se adueñó de ella. Se la encontró en el fondo del Mar Cerrado, entre los huesos de un cadáver, y se devolvió al Palacio Dorado donde sigue expuesta a día de hoy.",
            "Es fácil detenerse y sentir las olas, pero el buen equilibrio hay que buscarlo en movimiento y hacia adelante.",
            "Fueron los primigenios, creados por el fuego de la caja de Pondara. Del negro salió Tiranior, el más temido. Del verde nació Volaghar, el más rápido. Del rojo surgió Rinalian, la más astuta.",
            "Dicen que cada vez que se apaga el cielo nace una pesadilla, allá en el Sur.",
        ];

        // Function to select a random subtitle based on the theme
        function pickRandomSubtitle() {
            var bodyClass = document.body.className;
            var subtitles = lightSubtitles;

            if (bodyClass.includes('dark-theme')) {
                subtitles = darkSubtitles;
            }

            var randomIndex = Math.floor(Math.random() * subtitles.length);
            return subtitles[randomIndex];
        }

        // Function to update subtitles when the theme changes
        function updateSubtitles() {
            var randomSubtitle = pickRandomSubtitle();
            document.getElementById("randomSubtitle").textContent = randomSubtitle;
        }

        // Set a random subtitle when the page loads
        window.addEventListener('DOMContentLoaded', function() {
            updateSubtitles();
        });

        // Listen for changes to the theme picker and update subtitles accordingly
        document.querySelector('.theme-selector .body').addEventListener('click', function() {
            updateSubtitles();
        });