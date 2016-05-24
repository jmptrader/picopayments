# coding: utf-8
# Copyright (c) 2016 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


class ChannelAlreadyUsed(Exception):

    def __init__(self, channel_address, transactions):
        msg = "Channel '{0}' already used: '{1}'"
        super(ChannelAlreadyUsed, self).__init__(msg.format(
            channel_address, transactions
        ))


class InsufficientFunds(Exception):

    def __init__(self, needed, available):
        msg = "Needed funds '{0}', available '{1}'"
        super(InsufficientFunds, self).__init__(msg.format(needed, available))


class InvalidWif(Exception):

    def __init__(self, wif):
        msg = "Invalid wif: '{0}'"
        super(InvalidWif, self).__init__(msg.format(wif))


class InvalidPubKey(Exception):

    def __init__(self, pubkey):
        msg = "Invalid pubkey: '{0}'"
        super(InvalidPubKey, self).__init__(msg.format(pubkey))


class InvalidHexData(Exception):

    def __init__(self, hexdata):
        msg = "Invalid hexdata: '{0}'"
        super(InvalidHexData, self).__init__(msg.format(hexdata))


class InvalidString(Exception):

    def __init__(self, x):
        msg = "Invalid string: '{0}'"
        super(InvalidString, self).__init__(msg.format(x))


class InvalidHash160(Exception):

    def __init__(self, x):
        msg = "Invalid hash160: '{0}'"
        super(InvalidHash160, self).__init__(msg.format(x))


class InvalidSequence(Exception):

    def __init__(self, x):
        msg = "Invalid sequence: '{0}'"
        super(InvalidSequence, self).__init__(msg.format(x))


class InvalidInteger(Exception):

    def __init__(self, x):
        msg = "Invalid integer: '{0}'"
        super(InvalidInteger, self).__init__(msg.format(x))


class InvalidQuantity(Exception):

    def __init__(self, x):
        msg = "Invalid quantity: '{0}'"
        super(InvalidQuantity, self).__init__(msg.format(x))


class PubKeyUnpublished(Exception):

    def __init__(self, x):
        msg = "PubKey unpublished: '{0}'"
        super(PubKeyUnpublished, self).__init__(msg.format(x))
