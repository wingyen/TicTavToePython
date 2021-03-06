#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Msgs:


    WARMING = {
        "playerSetWrong": {
            'EN': "Please, follow the rules!",
            'PT-BR': "Por favor, siga as regras!",
            'CN':"请看游戏规则！"
        },

        "wrongMove": {
            'EN': u"%s \u2190 this move command is not allowed!",
            'PT-BR': u"%s \u2190 Esse comando é ínvalido!",
            'CN':u"%s \u2190 这种移动是不允许的。"

        },

        "coordUsed": {
            'EN': u"%s \u2190 This coordinate has already been used",
            'PT-BR': u"%s \u2190 Essa coordenada já foi usada",
            'CN':u"%s \u2190 这个坐标已经被占用。"
        }
    }

    ERROR = {
        "inputTypeIsWrong": {
            'EN' : "Make sure that you are using the right TYPE for this setting, anyway Default value will be used!",
            'PT-BR' : "Verifique o tipo usado na configuração, de qualquer forma a configuração será usada!",
            'CN': "请确认你输入正确，否则默认值会被使用。"
        },

        "playerValue": {
            'EN': "Only 1 character is accepted and can not be empty",
            'PT-BR': "Apenas 1 caractere é aceito e não pode ser vazio",
            'CN': "只能输入一个字母，而且不能留空。"
        }
    }

    UI = {

        "welcome": {
            'EN': u"\u2716 \u25CF \u25BC Welcome to Tic Tac Toe 2.0  \u25BC \u25CF \u2716\n:....... Good lunk and Have Fun ......:\n\n",
            'PT-BR': u"\u2716 \u25CF \u25BC Bem vindo ao Tic Tac Toe 2.0  \u25BC \u25CF \u2716\n:....... Boa sorte e divirta-se  ......:\n\n",
            'CN': u"\u2716 \u25CF \u25BC 欢迎来到 Tic Tac Toe 2.0 \u25BC \u25CF \u2716\n:....... 祝你好运！.......:\n\n"
        },

        "playerSizeChars": {
            'EN': "Min 2 characters",
            'PT-BR': "Min 2 caracteres",
            'CN': "至少2个字母"
        },

        "playerName": {
            'EN': "What is your name?",
            'PT-BR': "Qual é o nome do jogador?",
            'CN': "你的名字？"
        },

        "playerSet": {
            'EN': "Player %s has been set",
            'PT-BR': "O nome do jogador %s foi definido",
            'CN': "玩家 %s 已经被加入。"
        },

        "winnerAnnounce": {
            'EN': u"\n\n\uD83C\uDF81 \u01C3 %s - Player %s wins \u01C3 \uD83C\uDF81 \n\nThank you :)",
            'PT-BR': u"\n\n\uD83C\uDF81 \u01C3 %s - Jogador %s ganhou \u01C3 \uD83C\uDF81 \n\nObrigado :)",
            'CN':u"\n\n\uD83C\uDF81 \u01C3 %s -玩家 %s 赢了 \u01C3 \uD83C\uDF81 \n\n谢谢！:)"
        },

        "moveInstruction": {
            'EN': "(Move instruction: <Row,Column> (Nº between 0 and %s) ... ex 0,1)",
            'PT-BR': "(Instruções: <Linha,Coluna> (Nº entre 0 e %s) ... ex 0,1)",
            'CN': "移动规则：<行，列> （号码在 0 和 %s 之间）。。。例如 0,1"
        },

        "move": {
            'EN': "%s - Player Nº %s :: this is your turn, please make your move...",
            'PT-BR': "%s - Jogador Nº %s :: Esse é seu turno, faça sua jogada...",
            'CN': "%s - 玩家 Nº %s ：：轮到你了，请走下一步。。。"
        },

        "drawGame": {
            'EN': "There are no winners, the game ended in a draw. :/",
            'PT-BR': "Não há ganhador, o Jogo terminou empatado :/",
            'CN': "没有赢家，游戏以扯平结束。:/"
        },

        "announceTheWinner": {
            'EN': u"\n\n\U0001F389 \U0001F389 %s - Player %s wins \U0001F389 \U0001F389 \n\nObrigado :)",
            'PT-BR': u"\n\n\U0001F389 \U0001F389 %s - Jogador %s ganhou a partida \U0001F389 \U0001F389 \n\nObrigado :)",
            'CN': u"\n\n\U0001F389 \U0001F389 %s - 玩家 %s 赢了！\U0001F389 \U0001F389 \n\n 恭喜！"
        },



    }