# create a function to list the largest numbers 
    def find_m_max_probs(self, pl, m):
        # check if m is larger than # nodes 
        if m > len(pl):
            raise ValueError('m exceeds the number of existed nodes.')

        m_max_prob_nodes = []
        temp_max = math.inf
        while len(m_max_prob_nodes) < m:
            sub_pl = [x for x in pl if x < temp_max]
            temp_max = max(sub_pl)
            pos = [i for i, x in enumerate(sub_pl) if x == temp_max]
            m_max_prob_nodes.extend(pos)
            if len(m_max_prob_nodes) > m:
                m_max_prob_nodes = m_max_prob_nodes[:m]
                break

        return m_max_prob_nodes
