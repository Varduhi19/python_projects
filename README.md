<<<<<<< HEAD
# tnayin
=======
⚔️ Խնդիր․ «Text-Based MMORPG Battle Simulator (Game Engine)»Պատկերացրու տեքստային RPG խաղի շարժիչ (engine), որտեղ կերպարները պայքարում են միմյանց դեմ, ունեն հատուկ ունակություններ (skills), inventory, buffs/debuffs ու AI (արհեստական բանականություն)։📋 Ինչո՞վ է սա բարդ ու հետաքրքիր (OOP concepts)1. Polymorphism & Inheritance (Կերպարներ և Ունակություններ)Character (Base Class)․ Ունի health, mana, attack_power, use_skill():Warrior, Mage, Rogue (Child Classes)․ Ամեն մեկն ունի իր UNIQUE ունակությունները։Mage-ը կարող է կախարդանք անել (Fireball) և Mana ծախսել։Warrior-ը կարող է «Shield Block» անել ու վնասը (damage) քչացնել։Rogue-ը կարող է Dodge անել (խուսափել հարվածից) կամ Critical Hit անել։2. Decorator Pattern (Buffs & Debuffs)Կերպարի վրա կարող ես «դնել» վիճակներ, որոնք փոխում են նրա static status-ները․Poisoned (ամեն քայլի կորցնում է 5 HP):Frozen (բաց է թողնում իր քայլը):Berserk (Attack-ը դառնում է $2\times$, բայց Armor-ը դառնում է $0$):3. Magic Methods (Dunder Methods)hero1 + hero2 (__add__)․ Երկու կերպար «միանում են» թիմ ստեղծելու համար (Party)։hero1 > hero2 (__gt__)․ Ստուգում է, թե ով ավելի ուժեղ է (ըստ level-ի կամ overall power-ի)։__repr__․ Գեղեցիկ տպում է կերպարի status-ը (օրինակ՝ 🧙‍♂️ Gandalf [HP: 80/100 | MP: 45/50]):4. Event System (Observer Pattern)Երբ ինչ-որ մեկը մեռնում է կամ Critical Hit է անում, խաղը Log է գրում էկրանին (օրինակ՝ 💥 CRITICAL HIT! Mage hit Warrior for 45 damage!)։💡 Ինչպես կերևա խաղը (Output)Python# Ստեղծում ենք հերոսներին
gandalf = Mage(name="Gandalf", health=100, mana=50)
conan = Warrior(name="Conan", health=150, armor=20)

# Սկսվում է մարտը (Battle Loop)
arena = BattleArena(gandalf, conan)
arena.start_fight()

# Output-ը կլինի այսպիսին․
# 🧙‍♂️ Gandalf casts FIREBALL on 🗡️ Conan for 35 Magic Damage!
# 🗡️ Conan blocks 10 damage! Takes 25 damage. (HP: 125/150)
# 🗡️ Conan gets POISONED for 3 turns!
# ...
# 🏆 WINNER: Gandalf!

>>>>>>> eb0d0f9d1aec347d7dcf37da9daba0556fe42171
