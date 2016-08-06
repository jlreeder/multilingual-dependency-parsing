class Transition(object):
    """
    This class defines a set of transitions which are applied to a
    configuration to get the next configuration.
    """
    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'

    def __init__(self):
        raise ValueError('Do not construct this object!')

    @staticmethod
    def left_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """

        # Precondition: Neither the stack nor the buffer may be empty
        if not conf.buffer or not conf.stack:
            return -1

        # Precondition: Word on top of stack must not be the root (0)
        elif not conf.stack[-1]:
            return -1

        idx_wi = conf.buffer[0]
        idx_wj = conf.stack.pop()

        conf.arcs.append((idx_wi, relation, idx_wj))

    @staticmethod
    def right_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """

        # Precondition: Neither the stack nor the buffer are may be empty
        if not conf.buffer or not conf.stack:
            return -1

        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer.pop(0)

        conf.stack.append(idx_wj)
        conf.arcs.append((idx_wi, relation, idx_wj))

    @staticmethod
    def reduce(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """

        # Precondition: Neither the stack nor the buffer are empty
        # NOTE: This precondition does not seem to be necessary
        # if not conf.buffer or not conf.stack:
        #     return -1

        # Precondition: Fail if top of stack not the dependent of another word
        if conf.stack[-1] not in [dep[2] for dep in conf.arcs]:
            return -1

        conf.stack.pop()

    @staticmethod
    def shift(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """

        # Precondition: The buffer is not empty
        # NOTE: This precondition does not seem to be necessary
        # if not conf.buffer:
        #     return -1

        # Word at the top of the buffer moved to the stack
        top_buffer = conf.buffer.pop(0)
        conf.stack.append(top_buffer)
