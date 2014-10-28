class NoughtsAndCrossesView():
    def win(self):
        print 'Congratulations; you won!'

    def draw(self):
        print "It's a draw!"

    def report_error(self, message):
        print message

    def reset(self):
        board = ("+===+===+===+\n"
                 "|   |   |   |\n"
                 "+===+===+===+\n"
                 "|   |   |   |\n"
                 "+===+===+===+\n"
                 "|   |   |   |\n"
                 "+===+===+===+")
        print board
