# game/script.rpy:23
translate fr_FR story_463014ee:

    # "Oh. Hi. I guess you are here to learn about Ren'Py extensions... Give me a minute, will you?"
    "Oh. Bonjour. Je suppose que vous êtes là pour apprendre des choses sur les extensions Ren'Py... Un instant, je vous prie."

# game/script.rpy:24
translate fr_FR story_aae17319:

    # "I'm happy to see new faces here."
    "C'est un plaisir de voir de nouvelle têtes."

# game/script.rpy:25
translate fr_FR story_3e3b3dff:

    # "Did you know that Ren'Py extensions are nearly as old as Ren'Py itself?"
    "Saviez-vous que les extensions Ren'Py sont quasiment aussi vieilles que Ren'Py même ?"

# game/script.rpy:26
translate fr_FR story_fd4a6de1:

    # "They were added in 2007, only 2 years after Ren'Py's creation but a lack of documentation made them the exclusivity of a select few."
    "Elles existent depuis 2007, seulement 2 ans après la création de Ren'Py, mais un manque de documentation et d'exposition en a fait l'apanage de quelques élus."

# game/script.rpy:27
translate fr_FR story_1b609d08:

    # "That made sense though, they were intended as a mean to patch Ren'Py itself should an issue occur, not as something game developpers should use."
    "Cela avait du sens, cela dit. Leur objectif était à l'origine de permettre de corriger des problèmes dans Ren'Py même dusse une erreur fatale apparaître. Elles n'étaient pas prévues pour être utilisées par le plus grand nombre."

# game/script.rpy:28
translate fr_FR story_b78d1082:

    # "But maybe it's time for them to realize more of the potential they have despite their humble beginnings."
    "Mais peut-être qu'il est temps pour elles de réaliser le potentiel qu'elles ont toujours eu malgré leur objectif premier."

# game/script.rpy:30
translate fr_FR story_3a5720da:

    # "I made some research in this direction at the time. Where did I put those documents?{w=.5}.{w=.5}.{w=.5}.{w=1} Here they are, let's take a look."
    "J'avais fait des recherches pour atteindre cet objectif à l'époque. Où ai-je bien pu mettre mes papiers{w=.5}.{w=.5}.{w=.5}.{w=1} Les voilà ! Regardons ensemble, voulez-vous."

# game/script.rpy:33
translate fr_FR story_adf41934:

    # "I remember now. I had to create my extension files by hand at the time."
    "Je me souviens que je devais alors créer l'extension à la main à l'époque."

# game/script.rpy:34
translate fr_FR story_5ce9412e:

    # "If memory serves me right, I ended up learning how to create a script that I would always run from my extension's directory."
    "Si ma mémoire ne me fait pas défaut, j'avais fini par découvrir comment créer un script que je lançais systématiquement depuis le dossier dans lequel se trouvait mon extension."

# game/script.rpy:35
translate fr_FR story_f5e117cc:

    # "It was something like {color=#888}python -m zipfile -c ../game *{/color}."
    "Il ressemblait à ceci : {color=#888}python -m zipfile -c ../game *{/color}."

# game/script.rpy:36
translate fr_FR story_171df051:

    # "At some point I even learned how to run this script using only Ren'Py, but this time is far behind me now."
    "J'avais même fini par trouver un moyen de lancer ce script en utilisant exclusivement Ren'Py, mais la mémoire me fait défaut sur ce point."

# game/script.rpy:40
translate fr_FR story_a33f833e:

    # "Anyway, here are some of my old projects. I remember that they were based off the official documentation."
    "Quoi qu'il en soit, voici quelques-uns de mes vieux projets. Ils me semble qu'ils étaient basés sur la documentation officielle."

# game/script.rpy:41
translate fr_FR story_57c64c2c:

    # "I'm going to show them to you, however keep in mind that once you start looking at code, you will have to click down here to keep progressing."
    "Je vais vous les montrer, mais garder à l'esprit qu'une fois que vous commencerez à lire du code, il faudra cliquer ici pour pouvoir progresser."

# game/script.rpy:46
translate fr_FR story_1cc14f85:

    # "Here comes the first extension, it simply defines a custom warper that we can make use of.\nClick down here to progress..."
    "Voici la première extension, elle définit simplement un warper que nous pourrons utiliser plus tard.\nCliquez ici pour avancer..."

# game/script.rpy:47
translate fr_FR story_f2b51c96:

    # "You can take a look at its code by clicking the files listed on the right. First, click on {color=#888}examples/demo_warper.rpy{/color} and continue."
    "Vous pouvez regarder son code en cliquant sur les fichiers listés à droite. Commencez par cliquer sur {color=#888}examples/demo_warper.rpy{/color} puis continuez."

# game/script.rpy:48
translate fr_FR story_0648a007:

    # "This is a simple Ren'Py file that makes use of my extension, not the extension itself."
    "C'est un simple fichier Ren'Py qui utilise l'extension, pas l'extension même."

# game/script.rpy:49
translate fr_FR story_ead830c2:

    # "It declares a new image that is displayed in the {color=#888}demo_warper_example{/color} screen. Notice how it uses a {color=#888}linear_ext{/color} warper, which does not exist in Ren'Py."
    "Il crée une nouvelle image qui est affichée dans l'écran {color=#888}demo_warper_example{/color}. Voyez comme elle utilise le warper {color=#888}linear_ext{/color}, qui ne devrait pas exister dans Ren'Py."

# game/script.rpy:50
translate fr_FR story_d39020f8:

    # "Now open the file {color=#888}autorun.py{/color}. This file is mandatory in all Ren'Py extensions and is the one that is executed by Ren'Py when it loads the extension."
    "Maintenant, ouvrez {color=#888}autorun.py{/color}. Ce fichier est obligatoire dans toute extension Ren'Py et est celui exécuté par Ren'Py quand il charge l'extension."

# game/script.rpy:51
translate fr_FR story_bb531d9a:

    # "The first thing I did here is load renpy, as it is not available by default in an extension."
    "La première chose que j'y ai faite est d'importer renpy, car il n'est pas disponible par défaut dans les extensions."

# game/script.rpy:52
translate fr_FR story_4fc1b6c1:

    # "Then, I simply created the warper as the documentation recommends.{w=1} With one exception. Can you spot it?"
    "Ensuite, j'ai simplement créé le warper comme la documentation le recommandait.{w=1} A une exception près. La voyez-vous ?"

# game/script.rpy:53
translate fr_FR story_29783a6e:

    # "I changed the way I access the {color=#888}atl_warper{/color} decorator. In a rpy file, I would write {color=#888}@renpy.atl_warper{/color}, but it doesn't work the same way in extensions."
    "J'ai changé la manière de laquelle j'accédais au décorateur {color=#888}atl_warper{/color}. Dans un fichier rpy, J'écrirais {color=#888}@renpy.atl_warper{/color}, mais il n'en va pas de même dans les extensions."

# game/script.rpy:54
translate fr_FR story_a924a200:

    # "What is important in an extension is the way Ren'Py organizes its content, not the way it shows it when you are in a rpy file."
    "Ce qui importe dans une extension est la manière de laquelle Ren'Py organise son contenu, pas la manière de laquelle il la présente quand vous êtes dans un fichier rpy."

# game/script.rpy:55
translate fr_FR story_b3e0c31e:

    # "Il you want to use the same layout as from rpy files, you need to prepend the resource you want with {color=#888}renpy.store{/color}."
    "Si vous voulez utiliser la même organisation que dans un fichier rpy, il vous faudra ajouter {color=#888}renpy.store{/color} devant le chemin que vous voulez."

# game/script.rpy:56
translate fr_FR story_dde6d455:

    # "In this specific, you would need to write {color=#888}@renpy.store.renpy.atl_warper{/color}. I do not recommend you do, but it does work."
    "Dans le cas présent, il vous faudrait écrire {color=#888}@renpy.store.renpy.atl_warper{/color}. Je ne vous le recommande pas, mais cela marche."

# game/script.rpy:57
translate fr_FR story_d86e2718:

    # "Got it? Let's take a look at another extension that I wrote a bit later."
    "Avez-vous compris ? Parfait. Regardons une autre extension que j'ai créée un peu plus tard."

# game/script.rpy:62
translate fr_FR story_04f177db:

    # "This extension is a bit quirky, it randomly chooses a text option among many and only prints that one out. Look at {color=#888}examples/demo_label_random.rpy{/color} to see how to use it."
    "Cette extension est quelque peu surprenante. Elle choisit un texte au hasard dans une liste et n'affiche que celui-là. Regardez {color=#888}examples/demo_label_random.rpy{/color} pour voir comment l'utiliser."

# game/script.rpy:63
translate fr_FR story_8d95176d:

    # "Now open {color=#888}autorun.py{/color}. Do you see the {color=#888}from demo_random_label{/color} statement?"
    "Maintenant ouvrez {color=#888}autorun.py{/color}. Voyez-vous la ligne {color=#888}from demo_random_label{/color} ?"

# game/script.rpy:64
translate fr_FR story_42041b05:

    # "It imports the content of the file {color=#888}demo_label_random.py{/color} and registers the statement I use in {color=#888}examples/demo_label_random.rpy{/color} into Ren'Py."
    "Elle importe le contenu du fichier {color=#888}demo_label_random.py{/color} et enregistre l'instruction utilisée dans {color=#888}examples/demo_label_random.rpy{/color} dans Ren'Py."

# game/script.rpy:65
translate fr_FR story_e93c2f6f:

    # "Just like {color=#888}demo_label_random{/color}, any module can be made available to rpy files once it is declared in an extension file."
    "Tout comme {color=#888}demo_label_random{/color}, n'importe quel module peut être accessible depuis les fichiers Ren'Py dès lors qu'il existe dans une extension."

# game/script.rpy:66
translate fr_FR story_753bdc66:

    # "Keep in mind that any change you make to Ren'Py MUST be performed in your autorun, otherwise it might be lost and crash your game when reloading the game during developement."
    "Cependant, gardez à l'esprit que toute modification de Ren'Py DOIT être effectuée dans {color=#888}autorun.py{/color}, ou ils sont susceptibles d'être perdus et de provoquer des erreurs lors de rechargements du jeu."

# game/script.rpy:67
translate fr_FR story_d61a6ab2:

    # "Let's summon the example for this extension once, you can rollback and go forward again to see all potential texts, and then we will go over to a different example."
    "Appelons l'example de cette extension une fois, vous pourrez rollback et avancer pour voir les différents texte. Ensuite, nous passerons à l'exemple suivant."

# game/script.rpy:73
translate fr_FR story_f07b0019:

    # "This extension is a bit shy, move your cursor around the center of the screen to see what it does."
    "Cette extension est un peu timide, bouger votre souris au centre de l'écran pour voir ce qu'elle fait."

# game/script.rpy:74
translate fr_FR story_fae84070:

    # "It can be used in different ways, take a look at {color=#888}examples/demo_appearing.rpy{/color}, I created two screens that show the same thing but used my {color=#888}Appearing{/color} extension in different ways."
    "Elle peut être utilisée de nombreuses manières, regardez donc {color=#888}examples/demo_appearing.rpy{/color}. J'y ai créé deux écrans affichant la même chose mais ai utilisé l'extension {color=#888}Appearing{/color} de deux manières différentes."

# game/script.rpy:75
translate fr_FR story_5aefa4d5:

    # "The second one directly uses the Displayable's class, while the first one uses a custom screen label."
    "Le second écran utilise directement la classe du composant affichable, tandis que le premier utiliser une instruction d'écran spécifique."

# game/script.rpy:76
translate fr_FR story_a4d8d432:

    # "Could you open {color=#888}autorun.py{/color} so that I could tell you how I achieved this ?"
    "Pourriez-vous ouvrir {color=#888}autorun.py{/color} pour que je vous explique comment j'ai fait cela ?"

# game/script.rpy:77
translate fr_FR story_ae4ed876:

    # "Again, I created a module ({color=#888}demo_appearing{/color}) to store my Displayable, however if I did nothing I would have needed to import the module each time I wanted to use it."
    "A nouveau, j'ai créé un module ({color=#888}demo_appearing{/color}) pour déclarer mon composant, cependant, si je n'avais rien fait de plus il m'aurait fallu importer le module à chaque fois que je voulais l'utiliser."

# game/script.rpy:78
translate fr_FR story_909652b6:

    # "To avoid this, I added my Displayable to the store. Do you see the line starting with {color=#888}renpy.store{/color}? That's how you do it with static data."
    "Pour éviter ça, j'ai ajouté mon module au store. Voyez-vous la ligne qui commence par {color=#888}renpy.store{/color} ? C'est ainsi que j'ai fait."

# game/script.rpy:79
translate fr_FR story_9c9ce3d3:

    # "To add my Displayable to the screen Parser, I had to do a bit more. Everything else in the {color=#888}autorun.py{/color} is necessary to add it."
    "Pour ajouter mon composant au Parser d'écrans, il a fallu travailler un peu plus. A cette fin, tout ce que vous voyez dans {color=#888}autorun.py{/color} et dont nous n'avons pas encore parlé était nécessaire."

# game/script.rpy:80
translate fr_FR story_e4845af2:

    # "If you're curious, look at the comments I wrote at the time, my memory is pretty hazy."
    "Si vous êtes curieux, regardez donc les commentaires que j'avais laissés à l'époque. Je serais bien en peine de vous expliquer tout celà de tête."

# game/script.rpy:85
translate fr_FR story_1bb03b6a:

    # "That's about it for the basics, if you want to look at all the extensions I have on hand right now, you might want to take a look at my library"
    "C'est à peu près tout ce que je peux vous dire, si vous voulez voir les extensions que j'ai à disposition, regardez-donc dans ma bibliothèque"

# game/script.rpy:86
translate fr_FR story_732b83d4:

    # "I have put the extension I used to add colors to the files I showed you there, though you will have to understand its content on your own."
    "J'y ai mis l'extension qui m'a permis de vous montrer des textes colorés, mais il vous faudra comprendre son contenu par vous-même."

# game/script.rpy:87
translate fr_FR story_0cbe63f3:

    # "If you do look it up, stay far from the {color=#888}pygment{/color} directory, it is a module I didn't develop and is beyond the scope of this demo."
    "Si vous y jetez un oeil, évitez le dossier {color=#888}pygment{/color}. Il s'agit d'un module créé par d'autres et n'est pas le sujet qui vous intéressera a priori."

translate fr_FR strings:

    # game/script.rpy:9
    old "Story"
    new "Histoire"

    # game/script.rpy:9
    old "Library"
    new "Bibliothèque"

    # game/script.rpy:9
    old "Exit"
    new "Sortie"

