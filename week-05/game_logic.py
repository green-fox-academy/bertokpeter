class Logic:

    def battle(self, attacker, defender):
        self.strike(attacker, defender)
        self.strike(defender, attacker)

    def strike(self, attacker, defender):
        sv = attacker.sp + attacker.dice()*2
        if sv > defender.dp:
            defender.currenthp -= (sv-defender.dp)
        