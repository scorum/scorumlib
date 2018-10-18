operations = {
    'vote':                                       0,
    'comment':                                    1,

    'transfer':                                   2,
    'transfer_to_scorumpower':                    3,
    'withdraw_scorumpower':                       4,

    'account_create_by_committee':                5,
    'account_create':                             6,
    'account_create_with_delegation':             7,
    'account_update':                             8,

    'witness_update':                             9,
    'account_witness_vote':                       10,
    'account_witness_proxy':                      11,

    'delete_comment':                             12,
    'comment_options':                            13,
    'set_withdraw_scorumpower_route_to_account':  14,
    'set_withdraw_scorumpower_route_to_dev_pool': 15,

    'prove_authority':                            16,

    'request_account_recovery':                   17,
    'recover_account':                            18,
    'change_recovery_account':                    19,
    'escrow_approve':                             20,
    'escrow_dispute':                             21,
    'escrow_release':                             22,
    'escrow_transfer':                            23,

    'decline_voting_rights':                      24,
    'delegate_scorumpower_shares':                25,

    'create_budget':                              26,
    'close_budget':                               27,

    'proposal_vote':                              28,
    'proposal_create':                            29,

    'atomicswap_initiate':                        30,
    'atomicswap_redeem':                          31,
    'atomicswap_refund':                          32,

    'close_budget_by_advertising_moderator':      33,
    'update_budget':                              34,

    # betting
    "create_game": 48,
    "cancel_game": 49,
    "update_game_markets": 50,
    "update_game_start_time": 51,
    "post_game_results": 52,

    "post_bet_operation": 53,
    "cancel_pending_bets_operation": 54,

    # virtual operations
    'author_reward':                              35,
    'comment_benefactor_reward':                  36,
    'comment_payout_update':                      37,
    'comment_reward':                             38,
    'curation_reward':                            39,
    'hardfork':                                   40,
    'producer_reward':                            41,
    'active_sp_holders_reward':                   42,
    'return_scorumpower_delegation':              43,
    'shutdown_witness':                           44,
    'witness_miss_block':                         45,
    'expired_contract_refund':                    46,
    'acc_finished_vesting_withdraw':              47,
    'devpool_finished_vesting_withdraw':          48,
    'acc_to_acc_vesting_withdraw':                49,
    'devpool_to_acc_vesting_withdraw':            50,
    'acc_to_devpool_vesting_withdraw':            51,
    'devpool_to_devpool_vesting_withdraw':        52,
    'proposal_virtual':                           53,

    'budget_outgo':                               54,
    'budget_owner_income':                        55,
    'active_sp_holders_reward_legacy':            56,
    'budget_closing':                             57,

    'bets_matched_operation':                     58,
    'game_status_changed':                        59,
    'bet_resolved_operation':                     60,
    'bet_cancelled_operation':                    61,

    # proposal operations
    'registration_committee_add_member':          0,
    'registration_committee_exclude_member':      1,
    'registration_committee_change_quorum':       2,
    'development_committee_add_member':           3,
    'development_committee_exclude_member':       4,
    'development_committee_change_quorum':        5,
    'development_committee_withdraw_vesting':     6,
    'development_committee_transfer':             7,
    'development_committee_empower_advertising_moderator': 8,
    'development_committee_change_post_budgets_auction_properties': 9,
    'development_committee_change_banner_budgets_auction_properties': 10
}
