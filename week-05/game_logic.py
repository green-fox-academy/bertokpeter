class Logic:

    def battle(self, attacker, defender):
        self.strike(attacker, defender)
        if not defender.status == "dead":
            self.strike(defender, attacker)

    def strike(self, attacker, defender):
        sv = attacker.sp + attacker.dice()*2
        if sv > defender.dp:
            defender.currenthp -= (sv-defender.dp)
            if defender.currenthp <= 0:
                defender.currenthp = 0
                defender.status = "dead"
        