import argparse
import numpy as np
import os

from datautils import tgif_qa
from datautils import msrvtt_qa
from datautils import msvd_qa

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', default='tgif-qa', choices=['tgif-qa', 'msrvtt-qa', 'msvd-qa'], type=str)
    parser.add_argument('--answer_top', default=4000, type=int)
    parser.add_argument('--glove_pt',
                        help='glove pickle file, should be a map whose key are words and value are word vectors represented by numpy arrays. Only needed in train mode')
    parser.add_argument('--output_pt', type=str, default='data/{}/{}_{}_questions.pt')
    parser.add_argument('--vocab_json', type=str, default='data/{}/{}_vocab.json')
    parser.add_argument('--mode', choices=['train', 'val', 'test'])
    parser.add_argument('--question_type', choices=['frameqa', 'action', 'transition', 'count', 'none'], default='none')
    parser.add_argument('--seed', type=int, default=666)

    args = parser.parse_args()
    np.random.seed(args.seed)

    if args.dataset == 'tgif-qa':
        args.annotation_file = 'data/anetqa/data_{}.csv'
        args.output_pt = 'data/anetqa/{}/anetqa_{}_{}_questions.pt'
        args.vocab_json = 'data/anetqa/{}/anetqa_{}_vocab.json'
        # check if data folder exists
        if not os.path.exists('data/anetqa/{}'.format(args.question_type)):
            os.makedirs('data/anetqa/{}'.format(args.question_type))

        if args.question_type in ['frameqa', 'count']:
            tgif_qa.process_questions_openended(args)
        else:
            tgif_qa.process_questions_mulchoices(args)